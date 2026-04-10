from fastapi import FastAPI
from pydantic import BaseModel
from smart_env import SmartEnv

app = FastAPI()

env = SmartEnv()

# ✅ EXACT request schema
class StepRequest(BaseModel):
    action: str


@app.post("/reset")
def reset():
    state = env.reset()
    return {"observation": state}   # ⚠️ IMPORTANT KEY NAME


@app.post("/step")
def step(req: StepRequest):
    state, reward, done = env.step(req.action)
    return {
        "observation": state,   # ⚠️ NOT "state"
        "reward": reward,
        "done": done,
        "info": {}              # ⚠️ MUST INCLUDE
    }
