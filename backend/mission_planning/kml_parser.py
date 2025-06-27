"""
Handles KML file parsing and geofence logic for mission planning.
"""

import xml.etree.ElementTree as ET
import os

try:
    import utm
except ImportError:
    utm = None
    print("Warning: 'utm' package not installed. Coordinate conversion will not work.")

# Ray casting algorithm for point-in-polygon

def point_in_polygon(point, polygon):
    x, y = point
    n = len(polygon)
    inside = False
    p1x, p1y = polygon[0]
    for i in range(n+1):
        p2x, p2y = polygon[i % n]
        if min(p1y, p2y) < y <= max(p1y, p2y):
            if x <= max(p1x, p2x):
                if p1y != p2y:
                    xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                if p1x == p2x or x <= xinters:
                    inside = not inside
        p1x, p1y = p2x, p2y
    return inside

def parse_kml(file_path):
    """
    Parses a KML file from the given file_path and extracts area boundary coordinates (Polygon) and Points.
    Returns a dict: {'polygons': [list of polygons], 'points': [list of points]}
    """
    tree = ET.parse(file_path)
    root = tree.getroot()
    ns = {'kml': 'http://www.opengis.net/kml/2.2'}
    polygons = []
    points = []
    # Extract polygons
    for polygon in root.findall('.//kml:Polygon', ns):
        for coord in polygon.findall('.//kml:coordinates', ns):
            coord_text = coord.text.strip()
            poly = []
            for pair in coord_text.split():
                parts = pair.split(',')
                if len(parts) >= 2:
                    lon, lat = float(parts[0]), float(parts[1])
                    poly.append((lon, lat))
            if poly:
                polygons.append(poly)
    # Extract points
    for point in root.findall('.//kml:Point', ns):
        for coord in point.findall('.//kml:coordinates', ns):
            coord_text = coord.text.strip()
            for pair in coord_text.split():
                parts = pair.split(',')
                if len(parts) >= 2:
                    lon, lat = float(parts[0]), float(parts[1])
                    points.append((lon, lat))
    return {'polygons': polygons, 'points': points}

def convert_coordinates(coords):
    """
    Converts a list of (lon, lat) tuples to UTM coordinates using the utm package.
    Returns a list of (easting, northing, zone_number, zone_letter) tuples.
    """
    if utm is None:
        raise ImportError("utm package is not installed. Please install it with 'pip install utm'.")
    return [utm.from_latlon(lat, lon) for lon, lat in coords]

def check_geofence(position, boundary):
    """
    Checks if the position (lon, lat) is inside the given polygon boundary.
    """
    return point_in_polygon(position, boundary)

def auto_rth_on_breach(position, boundary):
    """
    Returns True if position is outside the boundary (should trigger RTH).
    """
    return not check_geofence(position, boundary)

# Example usage for any KML file
def demo_with_file(file_path):
    """
    Demonstrates parsing and geofence logic with the given KML file.
    Also tests with random points (not from KML) to check geofence logic.
    """
    kml_data = parse_kml(file_path)
    print('Polygons:', kml_data['polygons'])
    if kml_data['polygons']:
        boundary = kml_data['polygons'][0]
        print('\nConverted polygon boundary to UTM:')
        try:
            utm_boundary = convert_coordinates(boundary)
            print(utm_boundary)
        except Exception as e:
            print(f'UTM conversion error: {e}')
        # Test with random points (some inside, some outside)
        test_points = [
            (73.8320, 17.1759),   # likely inside
            (73.8318, 17.1761),   # likely inside
            (73.8330, 17.1765),   # outside
            (73.8317, 17.1758),   # on edge
            (73.8300, 17.1750),   # outside
        ]
        print('\nTesting random points:')
        for pt in test_points:
            inside = check_geofence(pt, boundary)
            print(f'Point {pt} inside boundary: {inside}')
            if auto_rth_on_breach(pt, boundary):
                print(f'Point {pt} is outside geofence! Trigger RTH.')
            try:
                utm_pt = convert_coordinates([pt])[0]
                print(f'Point {pt} in UTM: {utm_pt}')
            except Exception as e:
                print(f'UTM conversion error for point {pt}: {e}')

if __name__ == "__main__":
    # Use the script's directory for the KML file
    script_dir = os.path.dirname(os.path.abspath(__file__))
    kml_path = os.path.join(script_dir, 'test.kml')
    demo_with_file(kml_path) 