from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()

state = {
    "step": 0,
    "energy": 50
}

class Action(BaseModel):
    action: int

@app.post("/reset")
def reset():
    global state
    state = {"step": 0, "energy": 50}

    return {
        "observation": [state["energy"], state["step"]],
        "reward": 0,
        "done": False
    }

@app.post("/step")
def step(action: Action):
    global state

    state["step"] += 1

    if action.action == 1:
        state["energy"] += random.randint(-5, 5)
        reward = 1
    else:
        state["energy"] -= random.randint(0, 3)
        reward = 0

    done = state["step"] >= 10

    return {
        "observation": [state["energy"], state["step"]],
        "reward": reward,
        "done": done
    }
