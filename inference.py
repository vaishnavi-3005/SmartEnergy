import os
import time
import requests

# =========================
# ENV VARIABLES
# =========================
HF_TOKEN = os.getenv("HF_TOKEN")
MODEL_NAME = os.getenv("MODEL_NAME", "mistralai/Mistral-7B-Instruct")

API_URL = f"https://api-inference.huggingface.co/models/{MODEL_NAME}"

headers = {
    "Authorization": f"Bearer {HF_TOKEN}"
}

# =========================
# LOGGING
# =========================
def log(tag, msg):
    print(f"[{tag}] {msg}")

# =========================
# HF CALL FUNCTION
# =========================
def query_hf(prompt):
    response = requests.post(
        API_URL,
        headers=headers,
        json={"inputs": prompt}
    )

    result = response.json()

    # Handle HF response formats safely
    if isinstance(result, list):
        return result[0].get("generated_text", "")
    elif isinstance(result, dict):
        return result.get("generated_text", str(result))
    else:
        return str(result)

# =========================
# TASK RUNNER
# =========================
def run_task(task_name, prompt):
    log("START", f"Task: {task_name}")

    try:
        output = query_hf(
            f"You are an energy optimization agent.\n\nTask: {prompt}"
        )
    except Exception as e:
        output = f"ERROR: {str(e)}"

    log("STEP", f"Prompt: {prompt}")
    log("STEP", f"Output: {output}")

    score = min(1.0, len(output) / 100)

    log("END", f"Score: {score}")

    return score

# =========================
# MAIN
# =========================
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
        time.sleep(2)

    print("\nFINAL SCORE:", sum(results) / len(results))