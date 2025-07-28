import gym
from gym import spaces
import numpy as np

class ResponseEnv(gym.Env):
    def __init__(self, log_data):
        super().__init__()
        self.log_data = log_data
        self.current_index = 0

        # Example state: [severity_level: 0-2]
        self.observation_space = spaces.Discrete(3)

        # Actions: 0 = Ignore, 1 = Alert Admin, 2 = Quarantine IP, 3 = Isolate System
        self.action_space = spaces.Discrete(4)

    def _get_severity_level(self, severity):
        levels = {"Low": 0, "Medium": 1, "High": 2}
        return levels.get(severity, 0)

    def reset(self):
        self.current_index = 0
        state = self._get_severity_level(self.log_data[self.current_index]["severity"])
        return state

    def step(self, action):
        current = self.log_data[self.current_index]
        severity = current["severity"]
        true_action = current["ideal_action"]  # Supervised label for reward

        # Reward logic: +1 for match, -0.2 for wrong
        reward = 1.0 if action == true_action else -0.2

        self.current_index += 1
        done = self.current_index >= len(self.log_data)

        if not done:
            next_state = self._get_severity_level(self.log_data[self.current_index]["severity"])
        else:
            next_state = 0

        return next_state, reward, done, {}
