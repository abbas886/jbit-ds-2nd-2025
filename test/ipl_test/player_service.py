import json
import http
import requests

base_url = "http://localhost:3000/"

def get_all_players():
    response = requests.get(f"{base_url}players")
    players = response.json()
    return players

def get_player(id):
    response = requests.get(f"{base_url}players?id={id}")
    player = response.json()
    print(f"Player details of {id}:", player)
    return player
def add_player(id, name, team):
    if get_player(id) != []:
        return f"Player already exists with player id {id}"

    player = {
        "id": id,
        "name": name,
        "team": team
    }
    response = requests.post(f"{base_url}players/", json=player)
    print("After adding new record:", response.json())
    return response
def update_player(id, name, team):
    player = {
        "id": id,
        "name": name,
        "team": team
    }
    response = requests.put(f"{base_url}players", json=player)
    print("After updating record:", response.json())
    return response
def delete_player(id):
    if get_player(id) == []:
        return f"Player does not exist with player id {id}"
    response = requests.delete(f"{base_url}players/{id}")
    return response
def move_player_to_team(id, new_team):
    player = get_player(id)
    if player == []:
        return f"Player does not exist with player id {id}"
    
    player_data = player[0]
    player_data['team'] = new_team
    
    response = requests.put(f"{base_url}players", json=player_data)
    print("After moving player to new team:", response.json())
    return response
