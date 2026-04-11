import os
import time
from openai import OpenAI

API_BASE_URL = os.getenv("API_BASE_URL")
MODEL_NAME = os.getenv("MODEL_NAME")
HF_TOKEN = os.getenv("HF_TOKEN")

client = OpenAI(
    base_url=API_BASE_URL,
    api_key=HF_TOKEN
)


def log(tag, msg):
    print(f"[{tag}] {msg}")


def run_task(task_name, prompt):
    log("START", f"Task: {task_name}")

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": "You are an energy optimization agent."},
            {"role": "user", "content": prompt}
        ]
    )

    output = response.choices[0].message.content

    log("STEP", f"Prompt: {prompt}")
    log("STEP", f"Output: {output}")

    score = min(1.0, len(output) / 100)

    log("END", f"Score: {score}")

    return score


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

    print("FINAL SCORE:", sum(results) / len(results))