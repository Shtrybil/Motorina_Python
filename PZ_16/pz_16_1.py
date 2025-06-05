# Создайте класс «Круг», который имеет атрибут радиуса и методы для вычисления
# площади, длины окружности и диаметра.
import math


class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        return math.pi * self.r ** 2

    def circ(self):
        return 2 * math.pi * self.r

    def diam(self):
        return 2 * self.r
c1 = Circle(5)
c2 = Circle(10)

