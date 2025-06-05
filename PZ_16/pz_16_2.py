# Создание базового класса "Транспортное средство" и его наследование для создания
# классов "Автомобиль" и "Мотоцикл". В классе "Транспортное средство" будут
# общие свойства, такие как максимальная скорость и количество колес, а классы наследники будут иметь свои уникальные свойства и методы.
class Vehicle:
    def __init__(self, speed, wheels):
        self.speed = speed
        self.wheels = wheels

    def info(self):
        return f"Скорость: {self.speed}, Колёс: {self.wheels}"


class Car(Vehicle):
    def __init__(self, speed, wheels, brand, model):
        super().__init__(speed, wheels)
        self.brand = brand
        self.model = model

    def info(self):
        return f"Машина {self.brand} {self.model}, " + super().info()


class Bike(Vehicle):
    def __init__(self, speed, wheels, btype):
        super().__init__(speed, wheels)
        self.btype = btype

    def info(self):
        return f"Мотоцикл {self.btype}, " + super().info()

car = Car(200, 4, "Toyota", "Corolla")
bike = Bike(180, 2, "спорт")
print(car.info())
print(bike.info())