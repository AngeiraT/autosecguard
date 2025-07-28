from stable_baselines3 import PPO
from agents.rl.response_env import ResponseEnv

class RLResponseAgent:
    def __init__(self, model_path="agents/rl/rl_response_model"):
        self.model = PPO.load(model_path)

    def predict_response(self, severity):
        # Convert severity to level (0-2)
        level = {"Low": 0, "Medium": 1, "High": 2}.get(severity, 0)
        action, _ = self.model.predict(level)
        return self._map_action(action)

    def _map_action(self, action):
        return {
            0: "Ignore",
            1: "Alert Admin",
            2: "Quarantine IP",
            3: "Isolate System"
        }.get(action, "Ignore")

