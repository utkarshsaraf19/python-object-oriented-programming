import math


class Point:

    def __init__(self, x, y):
        self.move(x, y)

    def move(self, x, y):
        self.x = x
        self.y = y

    def reset(self):
        self.move(0, 0)

    def calculate_difference(self, another_point):
        return math.sqrt(((self.x - another_point.x) ** 2) + ((self.y - another_point.y) ** 2))
