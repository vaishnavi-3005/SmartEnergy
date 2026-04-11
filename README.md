# Smart Energy Optimization (OpenEnv)

##  Overview

This project implements a **Smart Energy Optimization Environment** using FastAPI, following the **OpenEnv pattern**.

It simulates an environment where an agent can take actions to optimize energy usage (lighting, AC, fan, etc.), and receive feedback.

An `inference.py` script is provided to simulate an AI agent interacting with the environment.

---

##  OpenEnv Concept

This project follows the Reinforcement Learning loop:

**Observe → Act → Reward → Repeat**

The environment exposes 3 core methods:

* `reset()` → Start a new episode
* `step(action)` → Take an action
* `state()` → Get current environment state

---

##  Project Structure

```
smart_energy_final/
│
├── server/
│   ├── app.py                      # FastAPI server
│   ├── smart_energy_final_environment.py
│   ├── client.py
│   ├── models.py
│
├── inference.py                    # Evaluation script
├── requirements.txt
└── README.md
```

---

## Setup Instructions

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

---

##  Run the Server

```bash
uvicorn server.app:app --reload
```

Open in browser:
http://127.0.0.1:8000/docs

---

## API Endpoints

| Method | Endpoint | Description       |
| ------ | -------- | ----------------- |
| GET    | `/reset` | Reset environment |
| POST   | `/step`  | Take action       |
| GET    | `/state` | Get current state |

---

## Example API Usage

### Reset

```bash
curl http://127.0.0.1:8000/reset
```

### Step

```bash
curl -X POST http://127.0.0.1:8000/step \
-H "Content-Type: application/json" \
-d '{"ac":1, "lights":1, "fan":0}'
```

### State

```bash
curl http://127.0.0.1:8000/state
```

---

## Run Inference Script

### Set environment variables (PowerShell)

```powershell
$env:HF_TOKEN="your_huggingface_token"
$env:MODEL_NAME="meta-llama/Meta-Llama-3-8B-Instruct"
```

### Run

```bash
python inference.py
```

---

## Output

The script runs 3 tasks:

* reduce_energy
* optimize_power
* efficiency_mode

Example output:

```
[START] Task: reduce_energy
[STEP] Output: Use LED lights and sensors...
[END] Score: 0.8

FINAL SCORE: 0.79
```

---

## Notes

* Do NOT hardcode API keys in code
* Use environment variables for tokens
* Ensure server is running before testing APIs

---

## Status

✔ FastAPI server working
✔ API endpoints tested
✔ Inference script working
✔ No secrets in repository

---

## Conclusion

This project demonstrates:

* OpenEnv-based environment design
* API-based RL interaction
* AI-driven evaluation via inference script

---

Ready for evaluation
