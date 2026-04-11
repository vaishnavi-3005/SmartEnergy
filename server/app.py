from fastapi import FastAPI
from server.smart_energy_final_environment import SmartEnergyFinalEnvironment

app = FastAPI()
env = SmartEnergyFinalEnvironment()

@app.get("/")
def home():
    return {"status": "Smart Energy Optimization Running "}


@app.get("/reset")
def reset():
    return env.reset()


@app.post("/step")
def step(data: dict):
    return env.step(data)


@app.get("/state")
def state():
    return env.state()
