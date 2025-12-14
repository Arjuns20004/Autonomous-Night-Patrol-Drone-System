
# telegram_alert.py
# Sends intrusion alerts via Telegram

import requests

BOT_TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"

def send_alert(location, label, lat, lon):
    message = (
        f"🚨 INTRUSION ALERT\n"
        f"Object: {label}\n"
        f"Location: {location}\n"
        f"Coordinates: {lat}, {lon}"
    )

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }

    try:
        requests.post(url, data=payload, timeout=5)
        print("[ALERT] Telegram message sent")
    except Exception as e:
        print("[ALERT ERROR]", e)
