from stable_baselines3 import PPO
from agents.rl.response_env import ResponseEnv
import json

# Load training data
with open("data/supervised_threats.json") as f:
    training_data = json.load(f)

env = ResponseEnv(training_data)
model = PPO("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=3000)

# Save trained model
model.save("agents/rl/rl_response_model")
