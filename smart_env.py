import random

class SmartEnv:

    def __init__(self):
        self.reset()

    def reset(self):
        self.state = {
            "time": random.choice(["morning","afternoon","evening","night"]),
            "temperature": random.randint(24, 35),
            "occupancy": random.randint(0, 5),
            "ac": random.randint(0, 1),
            "lights": random.randint(0, 1),
            "fan": random.randint(0, 1)
        }
        self.steps = 0
        return str(self.state)

    def step(self, action):

        if action == "turn_on_ac": self.state["ac"] = 1
        elif action == "turn_off_ac": self.state["ac"] = 0
        elif action == "turn_on_lights": self.state["lights"] = 1
        elif action == "turn_off_lights": self.state["lights"] = 0
        elif action == "turn_on_fan": self.state["fan"] = 1
        elif action == "turn_off_fan": self.state["fan"] = 0

        power = (6*self.state["ac"] + 2*self.state["lights"] + self.state["fan"])

        reward = -power

        if self.state["occupancy"] == 0 and power > 0:
            reward -= 5

        self.steps += 1
        done = self.steps >= 10

        return str(self.state), reward, done

    def close(self):
        pass