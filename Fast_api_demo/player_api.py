from fastapi import FastAPI 
from htt
from pydantic import BaseModel
from fastapi.responses import JSONResponse


app = FastAPI()
@app.get("/players/{player_id}")
def get_player(player_id: int):
    return {"player_id": player_id, "name": "Player Name", "team": "Team Name"}