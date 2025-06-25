from math import pi
from math import sqrt

class Shape:
    def __init__(self, base):
        self.base = base
        pass
    def get_area(self):
        pass
    def get_perimeter(self):
        pass
    def __str__(self):
        return f"{type(self).__name__}. area: {self.get_area()}. perimeter: {self.get_perimeter()}."

class Rectangle(Shape):
    def __init__(self,base, height):
        super().__init__(base=base)
        self.height = height
    def get_area(self):
        return self.base * self.height
    def get_perimeter(self):
        return  self.base * 2 + self.height * 2

class Square(Shape):
    def __init__(self, base):
        super().__init__(base=base)
    def get_area(self):
        return self.base * self.base
    def get_perimeter(self):
        return self.base * 4

class Triangle(Shape):
    def __init__(self, base, base2, base3):
        super().__init__(base=base)
        self.base2 = base2
        self.base3 = base3
    def get_area(self):
        s = self.base + self.base2 + self.base3
        x = s * (s - self.base) * (s - self.base2) * (s - self.base3)
        return sqrt(x)
    def get_perimeter(self):
        return self.base + self.base2 + self.base3


class Circle(Shape):
    def __init__(self,base):
        super().__init__(base=base)
    def get_area(self):
        return pi * self.base ** 2
    def get_perimeter(self):
        return pi * self.base * 2

class Hexagon(Shape):
    def __init__(self, base):
        super().__init__(base=base)
    def get_area(self):
        return (3 * sqrt(3) * self.base ** 2) / 2
    def get_perimeter(self):
        return self.base * 8

