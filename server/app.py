from fastapi import FastAPI
from inference import run_simulation
import uvicorn

app = FastAPI()

@app.post("/reset")
def reset():
    return {"status": "ok"}

@app.post("/step")
def step():
    result = run_simulation()
    return result

# ✅ REQUIRED for OpenEnv
def main():
    uvicorn.run(app, host="0.0.0.0", port=8000)

# ✅ REQUIRED
if __name__ == "__main__":
    main()