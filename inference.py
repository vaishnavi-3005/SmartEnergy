import os
import time
import requests

# -------------------------
# ENV CONFIG
# -------------------------
HF_TOKEN = os.getenv("HF_TOKEN")
API_URL = "https://router.huggingface.co/v1/chat/completions"
MODEL_NAME = os.getenv("MODEL_NAME", "mistralai/Mistral-7B-Instruct")

if not HF_TOKEN:
    raise ValueError("HF_TOKEN is missing. Set it using environment variable.")

headers = {
    "Authorization": f"Bearer {HF_TOKEN}",
    "Content-Type": "application/json"
}

# -------------------------
# LOGGING
# -------------------------
def log(tag, msg):
    print(f"[{tag}] {msg}")

# -------------------------
# TASK RUNNER
# -------------------------
def run_task(task_name, prompt):
    log("START", f"Task: {task_name}")

    payload = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "system", "content": "You are an energy optimization AI agent."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
        "max_tokens": 200
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        data = response.json()

        # extract output safely
        output = data["choices"][0]["message"]["content"]

    except Exception as e:
        output = f"ERROR: {str(e)}"

    log("STEP", f"Prompt: {prompt}")
    log("STEP", f"Output: {output}")

    # simple scoring (you can improve later)
    score = min(1.0, len(output) / 200)

    log("END", f"Score: {score}")

    return score

# -------------------------
# MAIN
# -------------------------
if __name__ == "__main__":

    tasks = [
        ("reduce_energy", "Minimize energy usage in lighting system"),
        ("optimize_power", "Optimize power distribution in smart grid"),
        ("efficiency_mode", "Improve system efficiency under constraints")
    ]

    results = []

    for name, prompt in tasks:
        score = run_task(name, prompt)
        results.append(score)
        time.sleep(1)

    print("\nFINAL SCORE:", sum(results) / len(results))