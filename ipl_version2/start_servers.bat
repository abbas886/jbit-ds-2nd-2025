@echo off
echo Starting JSON Server...
start cmd /k "json-server --watch ipl_db.json --port 3000"

echo Starting FastAPI Server 1...
start cmd /k "uvicorn team_api:app --reload --port 8001"

echo Starting FastAPI Server 2...
start cmd /k "uvicorn player_api:app --reload --port 8002"

echo Starting FastAPI Server 3...
start cmd /k "uvicorn match_api:app --reload --port 8003"

echo All servers started!
pause
