# 🌙🚁 Autonomous Night Patrol Drone System

An intelligent, Python-based autonomous drone patrol system designed for night-time security surveillance.  
The system performs real-time monitoring, detects intrusions using computer vision and AI, tracks drone movement live on a map, manages battery fail-safes, and generates alerts for security response.

---

## 🔍 Problem Statement
Manual night-time security patrols are inefficient, risky, and costly for large areas such as farms, campuses, warehouses, and restricted zones.  
There is a need for an automated, intelligent system that can patrol, detect intrusions, and respond proactively.

---

## 💡 Solution
This project implements an **Autonomous Night Patrol Drone System** that:
- Patrols predefined routes automatically
- Detects humans and animals during night surveillance
- Classifies threat levels
- Logs intrusion evidence
- Tracks drone movement live on a map
- Monitors battery health and triggers fail-safe actions

---

## ⚙️ Key Features
- 🌙 Night-time autonomous patrol
- 🧠 AI-based human & animal detection (YOLO-based)
- 🔍 Motion detection using OpenCV
- 🚨 Intrusion alert system
- 📸 Evidence capture with timestamp and location
- 🗺️ Live drone tracking on map (Flask + OpenStreetMap)
- 🔋 Battery monitoring with auto return-to-home fail-safe
- 📊 Web-based monitoring dashboard

---

## 🧰 Technology Stack
- **Programming Language:** Python  
- **Computer Vision:** OpenCV  
- **AI / ML:** YOLO (Ultralytics)  
- **Web Framework:** Flask  
- **Mapping:** Leaflet + OpenStreetMap  
- **Hardware (Conceptual):** Drone / Camera / Battery Sensor  

---

## 🧠 System Architecture
1. Drone follows predefined patrol waypoints  
2. Camera captures live feed  
3. Vision module detects motion and objects  
4. AI model classifies humans or animals  
5. Intrusions trigger alerts and evidence storage  
6. Drone location and battery are updated in real time  
7. Dashboard displays live status and map tracking  

---

## ▶️ How to Run
```bash
pip install -r requirements.txt
python main.py
