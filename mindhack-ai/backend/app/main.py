import os
from uuid import uuid4
from typing import Any
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field, ConfigDict, field_validator

app = FastAPI(title="MindVerse AI API", version="0.1.0", description="Local-first API for game configuration and minimized session summaries.")
origins = [o.strip() for o in os.getenv("CORS_ORIGINS", "http://localhost:5173,http://127.0.0.1:5173").split(",") if o.strip()]
app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=False, allow_methods=["GET", "POST"], allow_headers=["Content-Type"])

GAMES = [
 {"id":"gaze","name":"Gaze Quest","category":"visual_search","camera_optional":True,"description":"Click-based visual search; gaze metrics unavailable unless calibrated tracking is implemented."},
 {"id":"reaction","name":"Reaction Rush","category":"reaction_time","camera_optional":False,"description":"Reaction-time task using monotonic browser timestamps."},
 {"id":"memory","name":"Memory Matrix","category":"visual_memory","camera_optional":False,"description":"Repeat a short visual tile sequence."},
 {"id":"focus","name":"Focus Flow","category":"color_conflict","camera_optional":False,"description":"Choose ink color rather than word meaning."},
 {"id":"motion","name":"Motion Sync","category":"hand_eye","camera_optional":True,"description":"Mouse-mode target game; hand tracking may be unavailable in this build."},
]

class GameSummary(BaseModel):
    model_config = ConfigDict(extra="forbid")
    game_id: str
    score: float = Field(ge=0, le=100)
    valid_trials: int = Field(ge=0, le=1000)
    detail: str = Field(max_length=500, default="")
    metrics: dict[str, Any] = Field(default_factory=dict)

    @field_validator("game_id")
    @classmethod
    def known_game(cls, value: str) -> str:
        if value not in {g["id"] for g in GAMES}:
            raise ValueError("Unknown game_id")
        return value

    @field_validator("metrics")
    @classmethod
    def validate_metrics(cls, metrics: dict[str, Any]) -> dict[str, Any]:
        if len(metrics) > 30:
            raise ValueError("Too many metric fields")
        for key, value in metrics.items():
            if isinstance(value, (int, float)) and not isinstance(value, bool):
                if value < 0 or value > 1_000_000:
                    raise ValueError(f"Metric '{key}' is outside accepted range")
        return metrics

class SessionSummary(BaseModel):
    model_config = ConfigDict(extra="forbid")
    session_id: str | None = Field(default=None, max_length=80)
    games: list[GameSummary] = Field(min_length=1, max_length=5)
    note: str = Field(default="Session game summary; not a medical assessment.", max_length=300)

    @field_validator("games")
    @classmethod
    def unique_games(cls, games: list[GameSummary]) -> list[GameSummary]:
        ids = [g.game_id for g in games]
        if len(ids) != len(set(ids)):
            raise ValueError("Duplicate game summaries are not allowed")
        return games

@app.get("/api/health")
def health():
    return {"status": "ok", "service": "mindverse-ai-api", "version": "0.1.0"}

@app.get("/api/games")
def get_games():
    return {"games": GAMES}

@app.get("/api/config")
def get_config():
    return {"camera_processing": "browser-local by default", "persist_summaries": False, "diagnostic_use": False, "api_version": "0.1.0"}

@app.post("/api/results/validate")
def validate_results(summary: SessionSummary):
    return {"valid": True, "games_received": len(summary.games), "session_id": summary.session_id or str(uuid4()), "note": "Validated structure only; submitted scores are not independently verified."}

@app.post("/api/sessions/summary", status_code=202)
def submit_summary(summary: SessionSummary):
    # Intentionally does not persist data. The response confirms validation only.
    return {"accepted": True, "persisted": False, "session_id": summary.session_id or str(uuid4()), "games_received": len(summary.games), "message": "Summary validated; no data was stored."}

@app.get("/api/sessions/{session_id}")
def get_session(session_id: str):
    raise HTTPException(status_code=404, detail="Session persistence is disabled in this build.")
