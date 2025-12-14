
# patrol.py
# Handles waypoint navigation and patrol sequencing

import time
from detection import run_detection
from battery import drain_battery, get_battery_level
from shared_state import update_location

WAYPOINTS = [
    ("Gate Area", 12.9716, 77.5946),
    ("Warehouse Zone", 12.9720, 77.5950),
    ("Boundary Fence", 12.9725, 77.5955),
    ("Open Field", 12.9730, 77.5960)
]

def log_waypoints():
    print("[PATROL] Loaded waypoints:")
    for w in WAYPOINTS:
        print(" -", w[0])

def start_patrol():
    log_waypoints()
    for name, lat, lon in WAYPOINTS:
        print(f"[PATROL] Moving to {name}")
        update_location(lat, lon)
        time.sleep(2)

        print(f"[PATROL] Scanning {name}")
        run_detection(name, lat, lon)

        drain_battery(15)
        level = get_battery_level()
        print(f"[BATTERY] Level: {level}%")

        if level < 25:
            print("[FAILSAFE] Low battery detected")
            print("[FAILSAFE] Returning to base")
            break

        time.sleep(2)

    print("[PATROL] Patrol loop ended")
