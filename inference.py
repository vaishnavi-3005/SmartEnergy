import time

# -------------------------
# LOGGING
# -------------------------
def log(tag, msg):
    print(f"[{tag}] {msg}")

# -------------------------
# SIMPLE ENERGY AGENT (NO API)
# -------------------------
def generate_response(prompt):
    prompt = prompt.lower()

    if "lighting" in prompt:
        return "Use LED lights, motion sensors, and daylight optimization to reduce energy usage."

    elif "power" in prompt:
        return "Balance load distribution, use smart grids, and reduce peak demand for efficiency."

    elif "efficiency" in prompt:
        return "Optimize device usage, reduce wastage, and apply energy-saving algorithms."

    else:
        return "Apply general energy optimization techniques."

# -------------------------
# TASK RUNNER
# -------------------------
def run_task(task_name, prompt):
    log("START", f"Task: {task_name}")

    try:
        output = generate_response(prompt)
    except Exception as e:
        output = f"ERROR: {str(e)}"

    log("STEP", f"Prompt: {prompt}")
    log("STEP", f"Output: {output}")

    if "ERROR" in output or "API_ERROR" in output:
        score = 0.0
    else:
        score = min(1.0, len(output) / 100)

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