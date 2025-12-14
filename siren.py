
# siren.py
# Controls siren and spotlight (GPIO-ready)

def trigger_siren(label):
    if label == "person":
        print("🚨 HIGH THREAT - Siren ON")
        print("💡 Spotlight activated")
    else:
        print("⚠️ LOW THREAT - Silent monitoring")

def siren_off():
    print("🔕 Siren OFF")

def spotlight_off():
    print("💡 Spotlight OFF")
