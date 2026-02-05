from environment import TrafficEnvironment
from agent import QLearningAgent
import numpy as np

env = TrafficEnvironment()
agent = QLearningAgent()

episodes = 500

for ep in range(episodes):
    state = env.reset()
    done = False

    while not done:
        action = agent.choose_action(state)
        next_state, reward, done = env.step(action)
        agent.learn(state, action, reward, next_state)
        state = next_state

    if ep % 50 == 0:
        print(f"Episode {ep} completed")

np.save("q_table.npy", agent.q_table)
