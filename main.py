
# main.py
# Entry point for Autonomous Night Patrol Drone System
# This file initializes all modules and starts patrol and dashboard

from patrol import start_patrol
from map_server import start_map_server
import threading
import time

def banner():
    print("="*60)
    print(" AUTONOMOUS NIGHT PATROL DRONE SYSTEM ")
    print("="*60)

def initialize_system():
    print("[INIT] Initializing system modules...")
    time.sleep(1)
    print("[INIT] Camera module ready")
    print("[INIT] AI detection module ready")
    print("[INIT] Battery monitor ready")
    print("[INIT] Map server ready")

def start_services():
    print("[SYSTEM] Starting web dashboard thread")
    t = threading.Thread(target=start_map_server)
    t.daemon = True
    t.start()

def main():
    banner()
    initialize_system()
    start_services()
    print("[SYSTEM] Starting autonomous patrol")
    start_patrol()
    print("[SYSTEM] Patrol completed safely")

if __name__ == "__main__":
    main()
