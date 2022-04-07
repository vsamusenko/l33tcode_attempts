import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.input_balls = kwargs
        self.contents = []
        self.drawn_lst = []

        if len(kwargs) < 1:
            self.input_balls = {'red': 1}

        for color, num in self.input_balls.items():
            for i in range(num):
                self.contents.append(color)

    def draw(self, draw_amount):
        self.drawn_lst = []
        if draw_amount <= len(self.contents):
            self.drawn_lst = random.sample(self.contents, k=draw_amount)
            for i in self.drawn_lst:
                self.contents.remove(i)
        else:
            self.drawn_lst = self.contents[:]
            for i in self.drawn_lst:
                self.contents.remove(i)
        return self.drawn_lst

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    hat_contents = hat.contents[:]
    success = 0
    def draw():
        if num_balls_drawn <= len(hat_contents):
            drawn_balls = random.sample(hat.contents, k=num_balls_drawn)
        else:
            drawn_balls = hat_contents

        matches = 0
        for color, num in expected_balls.items():
            if drawn_balls.count(color) >= num:
                matches += 1
            else:
                matches += 0

        if matches == len(expected_balls):
            # print(drawn_balls)
            return 1
        else:
            # print(drawn_balls)
            return 0

    for i in range (num_experiments):
        if draw() > 0:
            success += 1

    return success / num_experiments





hat = Hat(blue=3,red=2,green=6)
probability = experiment(hat=hat, expected_balls={"blue":2,"green":1}, num_balls_drawn=4, num_experiments=1000)
print(probability)
