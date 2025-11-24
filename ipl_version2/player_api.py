# define all the end points related to player api and test through swagger ui
from fastapi import FastAPI

import player_service as service
import team_service as team_service

app = FastAPI()

@app.get("/")
def server_running():
    return "Player API Server is running..."


@app.get("/players")
def get_all_players():
    return service.get_all_players()

@app.get("/players/{player_id}")
def get_player_by_id(player_id: int):
    return service.get_player_by_id(player_id)

@app.get("/players/team/{team_name}")
def get_player_by_team(team_name: str):
    return service.get_player_by_team(team_name)

@app.post("/players")
def add_player(player_data: dict):
    # before hitting add_player of player_service from player_api,  hit team_service
    # (Call method which fetch all unique names)and check whether team exist or not.
    all_teams = team_service.get_all_team_names()
    if player_data['team'] not in all_teams:
        return {"error": "Team does not exist. Please provide a valid team."}

    return service.add_player(player_data)

@app.put("/players/{player_id}")
def update_player(player_id: int, player_data: dict):
    # we should check whether team exist or not before updating player details
    return service.update_player(player_id, player_data)

@app.delete("/players/{player_id}")
def delete_player(player_id: int):
    return service.delete_player(player_id)




