from math import pi
from math import sqrt

class Shape:
    def __init__(self, base):
        self.base = base
        pass
    def get_area(self):
        pass

class Rectangle(Shape):
    def __init__(self, base, height):
        super().__init__(base=base)
        self.height = height
    def get_area(self):
        return self.base * self.height

class Square(Shape):
    def __init__(self, base):
        super().__init__(base=base)
    def get_area(self):
        return self.base * self.base

class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__(base=base)
        self.height = height
    def get_area(self):
        return 0.5 * self.base * self.height

class Circle(Shape):
    def __init__(self, base):
        super().__init__(base=base)
    def get_area(self):
        return pi * self.base ** 2

class Hexagon(Shape):
    def __init__(self, base):
        super().__init__(base=base)
    def get_area(self):
        return (3 * sqrt(3) * self.base ** 2) / 2

