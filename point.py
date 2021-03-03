from math import *

class Point:
    def __init__(self, a, b):
        self.x = a
        self.y = b
    def printCoord(self):
        print((self.x, self.y))
    def translate(self, deltax, deltay):
        self.x += deltax
        self.y += deltay
    def odistance(self):
        return sqrt(self.x ** 2 + self.y ** 2)
    def __add__(self, p):
        return Point(self.x + p.x, self.y + p.y)


#  p = Point(3, 4)
#  p.printCoord()
#  print(p.odistance())
p1 = Point(3, 4)
p2 = Point(3, 4)
p3 = p1 + p2
p3.printCoord()
