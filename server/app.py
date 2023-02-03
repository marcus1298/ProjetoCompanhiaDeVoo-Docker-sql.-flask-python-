from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from datetime import datetime, timedelta

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'secret-key'
jwt = JWTManager(app)

# Dummy data to represent the airports and flights
airports = [{"id": 1, "name": "São Paulo - Guarulhos", "code": "GRU"},
            {"id": 2, "name": "Rio de Janeiro - Galeão", "code": "GIG"},
            {"id": 3, "name": "Belo Horizonte - Confins", "code": "CNF"},
            {"id": 4, "name": "Brasília - Juscelino Kubitschek", "code": "BSB"}]

flights = [{"id": 1, "origin": "GRU", "destination": "GIG", "departure_time": "2023-03-01T12:00:00", "price": 500.0},
           {"id": 2, "origin": "GRU", "destination": "CNF", "departure_time": "2023-03-01T14:00:00", "price": 400.0},
           {"id": 3, "origin": "GRU", "destination": "BSB", "departure_time": "2023-03-01T16:00:00", "price": 300.0},
           {"id": 4, "origin": "GIG", "destination": "GRU", "departure_time": "2023-03-02T12:00:00", "price": 500.0},
           {"id": 5, "origin": "CNF", "destination": "GRU", "departure_time": "2023-03-02T14:00:00", "price": 400.0},
           {"id": 6, "origin": "BSB", "destination": "GRU", "departure_time": "2023-03-02T16:00:00", "price": 300.0}]

# Endpoint to handle the user login
@app.route("/login", methods=["POST"])
def login():
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    
    # Dummy authentication - in a real implementation this would be a database check
    if email == "user@example.com" and password == "password":
        access_token = create_access_token(identity=email, expires_delta=timedelta(hours=1))
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"error": "Invalid username or password"}), 401

# Endpoint to handle the user logout
@app.route("/logout", methods=["POST"])
@jwt_required
def logout():
    jti = get_jwt_blacklist_token()
    jwt.blacklist_store.add_token_to_database(jti)
    return jsonify({"message": "Successfully logged out"}), 200

# Endpoint to return all available airports
@app.route("/airports", methods=["GET"])
def get_airports():
    return jsonify(airports), 200

# Endpoint to return all available flights
@app.route("/flights", methods=["GET"])
def get_flights():
    return jsonify(flights), 200

# Endpoint to return the details of a specific flight
@app.route("/flights/<int:flight_id>", methods=["GET"])
def get_flight(flight_id):
    for flight in flights:
        if flight["id"] == flight_id:
            return jsonify(flight), 200
    return jsonify({"error": "Flight not found"}), 404

# Endpoint to handle the reservation of a flight
@app.route("/reserve", methods=["POST"])
@jwt_required
def reserve():
    flight_id = request.json.get("flight_id", None)
    if flight_id is None:
        return jsonify({"error": "flight_id is required"}), 400
    for flight in flights:
        if flight["id"] == flight_id:
            return jsonify({"msg": "Flight reserved successfully", "flight_details": flight}), 200
    return jsonify({"error": "Flight not found"}), 404

if __name__ == "__main__":
    app.run()