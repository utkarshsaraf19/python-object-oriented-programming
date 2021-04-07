import math


class Point:
    """Represents the point in two dimensional coordinate"""

    def __new__(cls):
        """
        Constructor class which is called before object is created
        """
        print("Creating instance")
        return super(Point, cls).__new__(cls)

    # default values initializer
    def __init__(self, x=0, y=0):
        """
        Initialize the values of coordinate to (zero,zero) if not explicitly specified
        :param x: x coordinate
        :param y: y coordinate
        """
        self.move(x, y)

    def move(self, x, y):
        """
        Move the point to specified location
        :param x: point location on x axis
        :param y: point location on y axis
        :return: None
        """
        self.x = x
        self.y = y

    def reset(self):
        """
        rest the point ot (0,0)
        :return:
        """
        self.move(0, 0)

    def calculate_difference(self, another_point):
        """
        calculate the distance between two point using pythagorean theorem
        :param another_point: another instance of point class
        :return: distance between two points
        """
        return math.sqrt(((self.x - another_point.x) ** 2) + ((self.y - another_point.y) ** 2))
