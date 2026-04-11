import random

class SmartEnergyEnv:
    def __init__(self):
        self.state_data = {"step": 0, "energy": 100}

    def reset(self):
        self.state_data = {"step": 0, "energy": 100}
        return {"status": "reset", "state": self.state_data}

    def step(self, action):
        self.state_data["step"] += 1

        msg = action.get("message", "")

        # simple optimization simulation
        energy_used = len(msg) * random.uniform(0.5, 1.2)
        self.state_data["energy"] -= energy_used

        reward = max(0, 1 - (energy_used / 100))

        return {
            "step": self.state_data["step"],
            "energy": self.state_data["energy"],
            "reward": reward
        }

    def state(self):
        return self.state_data
