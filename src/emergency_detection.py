import random

print("\n===== EMERGENCY VEHICLE SYSTEM =====\n")

# Simulated detected vehicles
vehicles = [
    "car",
    "bus",
    "truck",
    "motorcycle",
    random.choice([
        "ambulance",
        "car",
        "bus"
    ])
]

print("Detected Vehicles:")

for vehicle in vehicles:
    print("-", vehicle)

# Emergency Detection
if "ambulance" in vehicles:

    print("\n🚑 EMERGENCY VEHICLE DETECTED")

    print("🚦 Traffic Signal Override Activated")

    print("🟢 Green Corridor Enabled")

    print("⚡ All Other Signals Set To RED")

    signal_status = "Emergency Mode"

else:

    print("\n✅ Normal Traffic Operation")

    signal_status = "Normal Mode"

print("\nSystem Status :", signal_status)