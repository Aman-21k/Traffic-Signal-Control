import random

class TrafficEnvironment:
    """
    Traffic Signal Environment for Reinforcement Learning
    """

    def __init__(self):
         self.max_cars = 50
         self.road_A = 0
         self.road_B = 0


    def reset(self):
        """
        Reset environment to initial state
        """
        self.road_A = random.randint(0, self.max_cars)
        self.road_B = random.randint(0, self.max_cars)
        return (self.road_A, self.road_B)

    def step(self, action):
        """
        Take an action and return next_state, reward, done

        Actions:
        0 -> Short green
        1 -> Medium green
        2 -> Long green
        """

        if action == 0:
            self.road_A -= 5
            self.road_B -= 2

        elif action == 1:
            self.road_A -= 10
            self.road_B -= 5

        elif action == 2:
            self.road_A -= 15
            self.road_B -= 10

        # Cars cannot be negative
        self.road_A = max(0, self.road_A)
        self.road_B = max(0, self.road_B)

        # Reward function
        reward = -(self.road_A + self.road_B)

        # Episode ends when traffic is cleared
        done = (self.road_A == 0 and self.road_B == 0)

        next_state = (self.road_A, self.road_B)

        return next_state, reward, done
