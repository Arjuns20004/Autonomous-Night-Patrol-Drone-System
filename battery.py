
# battery.py
# Battery monitoring and fail-safe handling

from shared_state import update_battery, get_state

def get_battery_level():
    return get_state()["battery"]

def drain_battery(amount):
    current = get_battery_level()
    new_level = current - amount

    if new_level < 0:
        new_level = 0

    update_battery(new_level)

def charge_battery():
    update_battery(100)

def battery_status_report():
    level = get_battery_level()
    if level > 75:
        return "HIGH"
    elif level > 40:
        return "MEDIUM"
    else:
        return "LOW"
