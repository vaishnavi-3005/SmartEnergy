from fastapi import FastAPI
from pydantic import BaseModel
from smart_env import SmartEnv

app = FastAPI()

env = SmartEnv()

class ActionRequest(BaseModel):
    action: str


# ✅ RESET
@app.post("/reset")
def reset():
    state = env.reset()
    return {
        "observation": str(state)   # ✅ FIXED
    }


# ✅ STEP
@app.post("/step")
def step(request: ActionRequest):
    state, reward, done = env.step(request.action)
    return {
        "observation": str(state),  # ✅ FIXED
        "reward": float(reward),
        "done": bool(done),
        "info": {}                 # ✅ VERY IMPORTANT
    }


# Optional
@app.get("/")
def home():
    return {"message": "API running"}
