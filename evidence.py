
# evidence.py
# Handles intrusion evidence storage

import cv2
import os
import datetime

BASE_DIR = "evidence"

def ensure_base():
    if not os.path.exists(BASE_DIR):
        os.makedirs(BASE_DIR)

def save_evidence(frame, location, label):
    ensure_base()
    folder = os.path.join(BASE_DIR, location.replace(" ", "_"))
    os.makedirs(folder, exist_ok=True)

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{label}_{timestamp}.jpg"
    path = os.path.join(folder, filename)

    cv2.imwrite(path, frame)
    print(f"[EVIDENCE] Saved {path}")
