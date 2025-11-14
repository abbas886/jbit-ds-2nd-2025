import requests
import json

base_url = "http://localhost:3000"

def get_players():
    response = requests.get(f"{base_url}/players")
    return response.json()  

def get_player_by_id(player_id):
    response = requests.get(f"{base_url}/players?id={player_id}")  
    return response.json()

def get_players_by_team(team_name):
    response = requests.get(f"{base_url}/players?team={team_name}")  
    return response.json() 
def add_player(player_data):
    if(get_player_by_id(player_data['id'] )):
        return {"error": "Player with this ID already exists."}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(f"{base_url}/players", data=json.dumps(player_data), headers=headers)
    return response.json()

# Need to update the url
def update_player(player_id, update_data):
    player = get_player_by_id(player_id )[0]
    if(not player):
        return {"error": "Player with this ID does not exist."}
    headers = {'Content-Type': 'application/json'}
    player["matches_played"] = update_data.get("matches_played")
    player["runs_scored"] = update_data.get("runs_scored")
    player["wickets_taken"] = update_data.get("wickets_taken")
                                                    
    response = requests.put(f"{base_url}/players/{player_id}", data=json.dumps(update_data), headers=headers)
    return response.json()

# delete player by id
def delete_player(player_id):
    response = requests.delete(f"{base_url}/players/{player_id}")
    return response.status_code == 200  


 

