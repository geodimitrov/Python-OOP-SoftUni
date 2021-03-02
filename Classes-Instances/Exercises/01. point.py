# Use dist() from math module to calc distance between points
from math import dist

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_x(self, new_x):
        self.x = new_x

    def set_y(self, new_y):
        self.y = new_y

    def distance(self, x, y):
        return dist((self.x, self.y), (x, y))


# Test Code
p = Point(2, 4)
p.set_x(3)
p.set_y(5)
print(p.distance(10, 2))

import unittest


class Tests(unittest.TestCase):
    def test_init(self):
        p = Point(20, 40)
        self.assertEqual(p.x, 20)
        self.assertEqual(p.y, 40)

    def test_set_x(self):
        p = Point(10, 20)
        p.set_x(7)
        self.assertEqual(p.x, 7)

    def test_set_y(self):
        p = Point(10, 20)
        p.set_y(18)
        self.assertEqual(p.y, 18)

    def test_distance(self):
        p = Point(10, 11)
        res = p.distance(5, 20)
        self.assertEqual(res, 10.295630140987)


if __name__ == "__main__":
    unittest.main()