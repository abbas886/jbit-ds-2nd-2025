from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import team_service as service
import player_service as player_service

app = FastAPI()

# Allow all origins OR restrict to your UI origin
origins = [
    "http://localhost",
    "http://127.0.0.1",
    "http://localhost:3000",
    "null"                    # <-- Important when loading HTML from file://
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,     # or ["*"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#http://localhost:8000/
@app.get("/")
def server_running():
    return "Team API Server is running..."

#http://localhost:8000/teams
@app.get("/teams")
def get_all_teams():
    return service.get_all_teams()
#http://localhost:8000/teams/{team_id}

@app.get("/teams/{team_id}")
def get_team_by_id(team_id: int):
    return service.get_team_by_id(team_id)

#http://localhost:8000/all_teams/names
@app.get("/all_teams/names")
def get_all_team_names():
    return service.get_all_team_names()

#http://localhost:8000/teams
@app.post("/teams")
def add_team(team_data: dict):
    return service.add_team(team_data)

#http://localhost:8000/teams/{team_id}
@app.put("/teams/{team_id}")
def update_team(team_id: int, team_data: dict):
    return service.update_team(team_id, team_data)

#http://localhost:8000/teams/{team_id}
@app.delete("/teams/{team_id}")
def delete_team(team_id: int):
    return service.delete_team(team_id)

#http://localhost:8000/teams/count
@app.get("/all_teams/count")
def get_team_count():
    return service.get_team_count()


#http://localhost:8000/teams/players/{team_name}
@app.get("/teams/players/{team_name}")
def get_players_by_team(team_name: str):
    # in player service we have to create a method get_players_by_team
    return player_service.get_player_by_team(team_name)

#http://localhost:8000/teams/top_scorer/{team_name}
@app.get("/teams/top_scorer/{team_name}")
def get_top_scorer_by_team(team_name: str):
    return service.get_top_scorer_by_team(team_name)

