import requests
import json

BASE_URL = "http://localhost:3000/matches"

def get_all_matches():
    response = requests.get(BASE_URL)
    return response.json()  

def get_match_by_id(match_id):
    response = requests.get(f"{BASE_URL}?id={match_id}")
    return response.json()

def get_matches_by_team(team_name):
    # if team1 or team2 is the given team_name
    #?team2=RCB&team1=RCB
    resp1 = requests.get(f"{BASE_URL}?team2={team_name}")
    resp2 = requests.get(f"{BASE_URL}?team1={team_name}")
    json1 =  resp1.json()
    json2 = resp2.json()
    return json1 + json2

def add_match(match_data):
    # check weather match already exists with same id
    if get_match_by_id(match_data['id']):
        return {"error": "Match with this ID already exists."}
    response = requests.post(BASE_URL, json=match_data)
    return response.json()
def update_match(match_id, match_data):
    if not get_match_by_id(match_id):
        return {"error": "Match not found."}
    response = requests.put(f"{BASE_URL}/{match_id}", json=match_data)

    if( response.status_code==200 ):
        return {"message": "Match updated successfully."}
    elif( response.status_code==404 ):
        return {"error": "Match not found."}
    elif( response.status_code==500 ):
        return {"error": "Internal server error."}   
                
    return response.json()

def delete_match(match_id):
    if not get_match_by_id(match_id):
        return {"error": "Match not found."}
    response = requests.delete(f"{BASE_URL}/{match_id}")

    if( response.status_code==200 ):
        return {"message": "Match deleted successfully."}
    else:
        return {"error": "Failed to delete match."}


