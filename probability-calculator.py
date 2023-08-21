import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, count in kwargs.items():
            self.contents.extend([color] * count)

    def draw(self, num_balls):
        drawn_balls = []
        if num_balls >= len(self.contents):
            drawn_balls = self.contents
            self.contents = []
        else:
            drawn_balls = random.sample(self.contents, num_balls)
            for ball in drawn_balls:
                self.contents.remove(ball)
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    num_successful = 0

    for _ in range(num_experiments):
        copy_hat = copy.deepcopy(hat)
        drawn_balls = copy_hat.draw(num_balls_drawn)

        drawn_balls_dict = {}
        for ball in drawn_balls:
            drawn_balls_dict[ball] = drawn_balls_dict.get(ball, 0) + 1

        success = True
        for color, count in expected_balls.items():
            if color not in drawn_balls_dict or drawn_balls_dict[color] < count:
                success = False
                break

        if success:
            num_successful += 1

    probability = num_successful / num_experiments
    return probability

