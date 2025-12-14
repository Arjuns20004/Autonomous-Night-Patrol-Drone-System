
# yolov8_detector.py
# AI-based object detection using YOLOv8

from ultralytics import YOLO

model = YOLO("yolov8n.pt")

def detect_objects(frame):
    results_list = []
    results = model(frame, verbose=False)

    for r in results:
        for box in r.boxes:
            cls_id = int(box.cls)
            label = model.names[cls_id]
            confidence = float(box.conf)

            if confidence > 0.5:
                results_list.append({
                    "label": label,
                    "confidence": confidence
                })

    return results_list
