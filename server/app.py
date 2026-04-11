from fastapi import FastAPI
from server.environment import SmartEnergyEnv

app = FastAPI()
env = SmartEnergyEnv()


@app.get("/reset")
def reset():
    return env.reset()


@app.post("/step")
def step(data: dict):
    return env.step(data)


@app.get("/state")
def state():
    return env.state()
