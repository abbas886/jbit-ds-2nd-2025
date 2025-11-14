from flask import Flask, jsonify, request
import requests
app = Flask(__name__)
BASE_URL = "http://localhost:3000"
@app.route('/players', methods=['GET'])
def get_players():
    print("Fetching all players")
    response = requests.get(f"{BASE_URL}/players")
    return jsonify(response.json())

@app.route('/players/<int:player_id>', methods=['GET'])
def get_player_by_id(player_id):
    print(f"Fetching player with ID: {player_id}")
    response = requests.get(f"{BASE_URL}/players?id={player_id}")
    return jsonify(response.json())

@app.route('/players', methods=['POST'])
def add_player():
    player_data = request.json
    print(f"Adding new player: {player_data}")
    response = requests.post(f"{BASE_URL}/players", json=player_data)
    return jsonify(response.json()), response.status_code
@app.route('/players/<int:player_id>', methods=['PUT'])
def update_player(player_id):
    update_data = request.json
    print(f"Updating player with ID: {player_id} with data: {update_data}")
    response = requests.put(f"{BASE_URL}/players/{player_id}", json=update_data)
    return jsonify(response.json()), response.status_code
@app.route('/players/<int:player_id>', methods=['DELETE'])
def delete_player(player_id):
    print(f"Deleting player with ID: {player_id}")
    response = requests.delete(f"{BASE_URL}/players/{player_id}")
    if response.status_code == 200:
        return jsonify({"message": "Player deleted successfully"}), 200
    else:
        return jsonify({"error": "Player not found"}), 404  

if __name__ == '__main__':
        app.run(debug=True)  # debug=True for development, disable in production
