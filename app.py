from flask import Flask, request, jsonify
from geopy.distance import geodesic

app = Flask(__name__)

# Data storage for each vehicle
vehicle_data = {}

# Destination (You can set any location - Example: Delhi)
DESTINATION = (28.7041, 77.1025)

@app.route("/update", methods=["POST"])
def update_vehicle():
    data = request.json
    vehicle_id = data["vehicle_id"]
    lat = data["lat"]
    lon = data["lon"]
    speed = data["speed"]

    # Calculate distance
    distance_km = geodesic((lat, lon), DESTINATION).km
    
    # Avoid division by zero
    if speed == 0:
        eta_minutes = None
    else:
        eta_minutes = (distance_km / speed) * 60

    # Save latest info
    vehicle_data[vehicle_id] = {
        "lat": lat,
        "lon": lon,
        "speed": speed,
        "distance_km": round(distance_km, 2),
        "eta_minutes": round(eta_minutes, 2) if eta_minutes else None
    }

    return {"status": "success"}

@app.route("/status", methods=["GET"])
def get_status():
    return jsonify(vehicle_data)

if __name__ == "__main__":
    app.run(port=5001)