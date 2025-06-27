# 🚀 Drone-Based Search and Rescue System

A robust software stack for autonomous mission planning, navigation, mapping, computer vision–based survivor detection, communication, and payload delivery for UAV-based search and rescue missions.

---

## 📑 Table of Contents

- [Overview](#overview)
- [File Structure](#file-structure)
- [Features](#features)
  - [A. Mission Planning & KML Integration](#a-mission-planning--kml-integration)
  - [B. Autonomous Navigation & Mapping](#b-autonomous-navigation--mapping)
  - [C. Computer Vision & Survivor Detection](#c-computer-vision--survivor-detection)
  - [D. Communication & Data Handling](#d-communication--data-handling)
  - [E. Ground Control Station (GCS) & Interface](#e-ground-control-station-gcs--interface)
  - [F. Payload Delivery (Delivery Drone)](#f-payload-delivery-delivery-drone)
  - [G. Safety, Compliance & Failsafes](#g-safety-compliance--failsafes)
  - [H. Testing & Validation](#h-testing--validation)
  - [I. Documentation & Reporting](#i-documentation--reporting)
- [Contributing](#contributing)
- [License](#license)

---

## 📖 Overview

This project delivers a complete software stack enabling autonomous drones to perform search and rescue operations. It supports mission planning with geofencing, real-time navigation and mapping using visual SLAM, AI-powered survivor detection, secure telemetry communication, payload delivery, and integration with a Ground Control Station (GCS).

---

## 📂 File Structure

- backend/
  - mission_planning/
    - __init__.py
    - kml_parser.py
  - navigation/
    - __init__.py
    - slam.py
  - computer_vision/
    - __init__.py
    - survivor_detection.py
  - Readme.md

---

## ⭐ Features

### A. Mission Planning & KML Integration

- Parse KML files to extract area boundary coordinates
- Convert KML coordinates to GPS/UTM for onboard processing
- Implement geofence logic to prevent out-of-bounds flight
- Auto-trigger Return-to-Home (RTH) on geofence breach
- Validate geofence with simulated/test coordinates

---

### B. Autonomous Navigation & Mapping

- Set up and optimize visual SLAM (e.g., ORB-SLAM3) for real-time mapping
- Integrate GPS and IMU data for scale correction and robustness
- Test SLAM accuracy and drift in controlled environments
- Develop area coverage algorithms (lawnmower/spiral) for full scan within time limits
- Integrate path planner with geofence and SLAM outputs

---

### C. Computer Vision & Survivor Detection

- Select and optimize YOLO (or equivalent) model for aerial human detection
- Collect and augment training data for rooftop human detection scenarios
- Train and validate detection models; optimize for Raspberry Pi
- Integrate detection pipeline with live camera feed
- Fuse detection results with SLAM/GPS for geotagging survivors

---

### D. Communication & Data Handling

- Set up LoRa module for telemetry and survivor geotag transmission
- Define data packet structure and implement error handling
- Integrate communication link with the Ground Control Station (GCS)
- Ensure all mission data (status, location, detections) is reported to GCS

---

### E. Ground Control Station (GCS) & Interface

- Develop interface to display real-time drone positions and survivor locations
- Integrate mission status and command controls as per rulebook
- Implement a single interface for both drones to comply with competition rules
- Test GCS with simulated mission data

---

### F. Payload Delivery (Delivery Drone)

- Implement waypoint navigation to survivor coordinates
- Integrate servo-based payload drop mechanism with flight controller
- Confirm delivery via onboard sensors (e.g., camera, IMU)
- Report delivery status to GCS

---

### G. Safety, Compliance & Failsafes

- Implement RTH and battery failsafe logic
- Test geofence and altitude breach responses
- Log all mission-critical events for pre-flight inspection and review

---

### H. Testing & Validation

- Unit test each subsystem (navigation, computer vision, communications, delivery)
- Conduct integration testing on the full software stack
- Perform field trials with mock survivors and KML-defined boundaries
- Track metrics such as detection accuracy, mapping precision, delivery accuracy, and overall system stability

---

### I. Documentation & Reporting

- Document all APIs, algorithms, and overall system architecture
- Maintain logs of tests, code changes, and hardware modifications
- Prepare technical review and business pitch presentations as per competition deliverables

---

## 🤝 Contributing

Contributions are welcome! Please fork the repository, make changes, and submit a pull request. For major changes, open an issue first to discuss your proposal.

---

## 📜 License

This project is licensed under the MIT License.
