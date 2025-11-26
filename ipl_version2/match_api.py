from fastapi import FastAPI
import match_service as service
import team_service as team_service
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

#Allow all origins OR restrict to your UI origin
origins = [
    "http://localhost",
    "http://127.0.0.1",
    "http://127.0.0.1:5500",
    "http://localhost:3000",
    "http://localhost:5500",
    
    "null"                    # <-- Important when loading HTML from file://
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,     # or ["*"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# server running check
@app.get("/")
def server_running():
    return "Match API Server is running..."

@app.get("/matches")
def get_all_matches():
    return service.get_all_matches()

@app.get("/matches/{match_id}")
def get_match_by_id(match_id: int):
    return service.get_match_by_id(match_id)

@app.get("/matches/team/{team_name}")
def get_matches_by_team(team_name: str):
    return service.get_matches_by_team(team_name)

@app.post("/matches")
def add_match(match_data: dict):
   if( team_service.get_team_by_name(match_data['team1']) and  team_service.get_team_by_name(match_data['team2']) ):
     return service.add_match(match_data)
   return "Teams does not exist, we cant add match"
  

@app.put("/matches/{match_id}")
def update_match(match_id: int, match_data: dict):
    return service.update_match(match_id, match_data)

@app.delete("/matches/{match_id}")
def delete_match(match_id: int):
    return service.delete_match(match_id)





