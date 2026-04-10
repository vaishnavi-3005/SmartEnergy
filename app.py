from fastapi import FastAPI
from pydantic import BaseModel
from smart_env import SmartEnv

app = FastAPI()

env = SmartEnv()

# Define request model (IMPORTANT)
class ActionRequest(BaseModel):
    action: str


@app.post("/reset")
def reset():
    state = env.reset()
    return {"state": state}


@app.post("/step")
def step(req: ActionRequest):
    state, reward, done = env.step(req.action)
    return {
        "state": state,
        "reward": reward,
        "done": done
    }
