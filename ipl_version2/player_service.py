import requests
import json
BASE_URL = "http://localhost:3000/players"


def get_all_players():
    response = requests.get(BASE_URL)
    return response.json()

def get_player_by_id(player_id):
    response = requests.get(f"{BASE_URL}?id={player_id}")
    return response.json()

def get_player_by_team(team_name):

    response = requests.get(f"{BASE_URL}?team={team_name}")
    return response.json()

def add_player(player_data):
    # check weather player already exists with same id
    if get_player_by_id(player_data['id']):
        return {"error": "Player with this ID already exists."}
    response = requests.post(BASE_URL, json=player_data)
    return response.json()

def update_player(player_id, player_data):
    if not get_player_by_id(player_id):
        return {"error": "Player not found."}
    response = requests.put(f"{BASE_URL}/{player_id}", json=player_data)  # working
    return response.json()

def delete_player(player_id):
    if not get_player_by_id(player_id):
        return {"error": "Player not found."}
    response = requests.delete(f"{BASE_URL}/{player_id}")

    if( response.status_code):
        return {"message": "Player deleted successfully."}
    else:
        return {"error": "Failed to delete player."}
    




   



