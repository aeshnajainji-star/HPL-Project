import time
import requests
import random

# Starting point
lat = 28.6139
lon = 77.2090

while True:
    # Simulate movement
    lat += random.uniform(-0.0005, 0.0005)
    lon += random.uniform(-0.0005, 0.0005)

    data = {
        "vehicle_id": "V1",
        "lat": lat,
        "lon": lon,
        "speed": random.randint(20, 60)
    }

    print("Sending:", data)

    try:
        requests.post("http://127.0.0.1:5001/update", json=data)
    except Exception as e:
        print("Error sending data:", e)

    time.sleep(1)