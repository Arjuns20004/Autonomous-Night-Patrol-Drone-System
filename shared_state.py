
# shared_state.py
# Shared real-time drone state

drone_state = {
    "lat": 12.9716,
    "lon": 77.5946,
    "battery": 100
}

def update_location(lat, lon):
    drone_state["lat"] = lat
    drone_state["lon"] = lon

def update_battery(value):
    drone_state["battery"] = value

def get_state():
    return drone_state

def reset_state():
    drone_state["battery"] = 100
