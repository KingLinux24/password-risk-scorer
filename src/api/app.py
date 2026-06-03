from fastapi import FastAPI
from pydantic import BaseModel
from src.scoring.risk import score

app = FastAPI(title="Password Risk Scorer", version="1.0")

class PasswordInput(BaseModel):
    password: str

@app.post("/score")
def score_password(payload: PasswordInput):
    result = score(payload.password)
    return result
