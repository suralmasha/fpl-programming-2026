"""
O - Open/Closed Principle (Принцип открытости/закрытости)
Нужен при расширении функционала
"""

import math
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


# НЕ ИЗМЕНЯЕМ БАЗОВЫЙ КЛАСС, а добавляем новые фигуры через наследование и полиморфизм
# Наследование и полиморфизм здесь - один из способов, а не обязательное условие

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2


shapes = [Rectangle(2, 3), Circle(5)]
for shape in shapes:
    print(f'Area: {shape.area()}')