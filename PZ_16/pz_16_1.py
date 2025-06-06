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
c3 = Circle(20)

print(f"Круг 1: радиус {c1.r}")
print(f"- Площадь: {c1.area():.2f}")
print(f"- Длина окружности: {c1.circ():.2f}")
print(f"- Диаметр: {c1.diam()}")

print(f"\nКруг 2: радиус {c2.r}")
print(f"- Площадь: {c2.area():.2f}")
print(f"- Длина окружности: {c2.circ():.2f}")
print(f"- Диаметр: {c2.diam()}")

print(f"\nКруг 3: радиус {c3.r}")
print(f"- Площадь: {c3.area():.2f}")
print(f"- Длина окружности: {c3.circ():.2f}")
print(f"- Диаметр: {c3.diam()}")