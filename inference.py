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

    if "occupancy': 0" in state:
        return "turn_off_ac"

    return "turn_on_ac"


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