
# detection.py
# Handles camera feed, motion detection and AI object detection

import cv2
import time
from yolov8_detector import detect_objects
from evidence import save_evidence
from telegram_alert import send_alert
from siren import trigger_siren

cap = cv2.VideoCapture(0)

def initialize_camera():
    if not cap.isOpened():
        print("[ERROR] Camera not accessible")
    else:
        print("[CAMERA] Camera initialized")

def run_detection(location, lat, lon):
    initialize_camera()
    start_time = time.time()

    while time.time() - start_time < 6:
        ret, frame = cap.read()
        if not ret:
            print("[ERROR] Frame capture failed")
            break

        detections = detect_objects(frame)

        for obj in detections:
            label = obj["label"]
            print(f"[DETECT] {label} detected at {location}")

            save_evidence(frame, location, label)
            send_alert(location, label, lat, lon)
            trigger_siren(label)

        cv2.imshow("Night Patrol Feed", frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break

    cv2.destroyAllWindows()
