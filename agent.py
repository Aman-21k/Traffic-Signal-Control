import numpy as np
import random

class QLearningAgent:
    def __init__(self):
        self.q_table = np.zeros((51, 51, 3))
        self.alpha = 0.1
        self.gamma = 0.9
        self.epsilon = 0.2

    def choose_action(self, state):
        if random.random() < self.epsilon:
            return random.randint(0, 2)
        return np.argmax(self.q_table[state[0], state[1]])

    def learn(self, state, action, reward, next_state):
        predict = self.q_table[state[0], state[1], action]
        target = reward + self.gamma * np.max(
            self.q_table[next_state[0], next_state[1]]
        )
        self.q_table[state[0], state[1], action] += self.alpha * (target - predict)
