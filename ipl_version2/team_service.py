# import related libraries
import requests
import json

BASE_URL = "http://localhost:3000/teams"

# fetch all teams (with all the properties/keys)
def get_all_teams():
    response = requests.get(BASE_URL)
    return response.json()

# fetch all unique team names
def get_all_team_names():   
    teams = get_all_teams()
    team_names = set()    # set does not all duplicate values
    for team in teams:
        team_names.add(team['name'])
    return list(team_names)

def get_team_by_id(team_id):
    response = requests.get(f"{BASE_URL}?id={team_id}")
    return response.json()

def get_team_by_name(team_name):
    response = requests.get(f"{BASE_URL}?name={team_name}")
    return response.json()

def get_team_count():
    teams = get_all_teams()
    return len(teams)

def add_team(team_data):
    # check weather team already exists with same id
    if get_team_by_id(team_data['id']):
        return {"error": "Team with this ID already exists."}
    response = requests.post(BASE_URL, json=team_data)
    return response.json()
def update_team(team_id, team_data):
    if not get_team_by_id(team_id):
        return {"error": "Team not found."}
    response = requests.put(f"{BASE_URL}/{team_id}", json=team_data)
    return response.json()

def delete_team(team_id):
    if not get_team_by_id(team_id):
        return {"error": "Team not found."}
    response = requests.delete(f"{BASE_URL}/{team_id}")

    if( response.status_code==200 ):
        return {"message": "Team deleted successfully."}
    else:
        return {"error": "Failed to delete team."}

