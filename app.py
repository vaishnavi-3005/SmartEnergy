from fastapi import FastAPI
from pydantic import BaseModel
from smart_env import SmartEnv

app = FastAPI()

env = SmartEnv()

class StepRequest(BaseModel):
    action: str

@app.post("/reset")
def reset():
    return {"observation": env.reset()}

@app.post("/step")
def step(req: StepRequest):
    state, reward, done = env.step(req.action)
    return {
        "observation": state,
        "reward": reward,
        "done": done,
        "info": {}
    }
