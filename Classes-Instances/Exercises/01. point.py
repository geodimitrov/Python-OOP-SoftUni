import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_x(self, new_x):
        self.x = new_x

    def set_y(self, new_y):
        self.y = new_y

    def distance(self, x, y):
        a = self.x - x
        b = self.y - y
        return math.sqrt(a ** 2 + b ** 2)


# # Test Code
p = Point(2, 4)
p.set_x(3)
p.set_y(5)
print(p.distance(10, 2))
p_2 = Point(10, 11)
print(p_2.distance(5, 20))