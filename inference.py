from smart_env import SmartEnv

def log_start():
    print("[START] task=smart-energy env=custom model=rule", flush=True)
    print("\n Starting Smart Energy Simulation...\n")

def log_step(step, action, reward, done):
    # Required format (DO NOT CHANGE)
    print(f"[STEP] step={step} action={action} reward={reward:.2f} done={str(done).lower()} error=null", flush=True)

    # Extra human-friendly output
    print(f"    Step {step}: Action = {action}")
    print(f"      Reward = {reward} ({'Good' if reward > -3 else 'Bad'})")
    print(f"      Status = {'Finished' if done else 'Running'}\n")

def log_end(success, steps, score, rewards):
    r = ",".join(f"{x:.2f}" for x in rewards)
    
    print(f"[END] success={str(success).lower()} steps={steps} score={score:.2f} rewards={r}", flush=True)

    print("\nFINAL SUMMARY")
    print("------------------------")
    print(f"Total Steps: {steps}")
    print(f"Final Score: {score:.2f}")
    print(f"Success: {'YES ' if success else 'NO '}")
    print(f"Average Reward: {sum(rewards)/len(rewards):.2f}")


def smart_policy(state):

    # Convert string to dictionary
    state_dict = eval(state)

    occupancy = state_dict["occupancy"]
    temp = state_dict["temperature"]

    # Smarter decisions
    if occupancy == 0:
        return "turn_off_ac"
    
    if temp > 30:
        return "turn_on_ac"
    
    if temp < 26:
        return "turn_off_ac"
    
    return "turn_on_fan"


def main():

    env = SmartEnv()

    rewards = []

    log_start()

    state = env.reset()

    for step in range(1, 11):

        action = smart_policy(state)

        state, reward, done = env.step(action)

        rewards.append(reward)

        log_step(step, action, reward, done)

        if done:
            break

    score = min(max(sum(rewards)/50, 0), 1)
    success = score > 0.3

    env.close()

    log_end(success, step, score, rewards)


if __name__ == "__main__":
    main()


# inference.py

def run_simulation(steps: int): 
    """
    Runs the Smart Energy Simulation for a given number of steps.

    Args:
        steps (int): Maximum number of steps to run the simulation.

    Returns:
        dict: Dictionary containing steps, score, success, average reward, logs, and rewards list.
    """
    env = SmartEnv()
    rewards = []
    logs = []

    logs.append("[START] Smart Energy Simulation\n")

    state = env.reset()

    for step in range(1, steps + 1):  # use user-defined steps
        action = smart_policy(state)
        state, reward, done = env.step(action)

        rewards.append(reward)

        log_line = f"[STEP] step={step} action={action} reward={reward:.2f} done={str(done).lower()}"
        logs.append(log_line)

        if done:
            break

    # Score calculation
    score = min(max(sum(rewards)/50, 0), 1)
    success = score > 0.3

    logs.append(f"\n[END] success={str(success).lower()} steps={step} score={score:.2f}")

    env.close()

    return {
        "steps": step,
        "score": round(score, 2),
        "success": success,
        "avg_reward": round(sum(rewards)/len(rewards), 2),
        "logs": "\n".join(logs),
        "rewards": rewards
    }
