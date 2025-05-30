import math
from abc import ABC, abstractmethod

class Figure(ABC):
    '''Абстрактный класс для фигур'''

    @abstractmethod
    def square(self):
        '''абастрактный метод для определения площади'''
        pass


class Circle(Figure):
    '''Класс для окружности'''

    def __init__(self, radius: int | float) -> None:
        '''Создаем экземпляр окружности, передаем в него радус'''
        self.radius = radius

    def square(self) -> float:
        '''вычисляем площадь окружности'''
        return math.pi * pow(self.radius, 2)


class Triangle(Figure):
    '''Класс для треугольника'''

    def __init__(self, a: int | float, b: int | float, c: int | float):
        '''Создаем экземпляр треугольника, передаем в него стороны'''
        self.a, self.b, self.c = a, b, c
        self._validate()

    def _validate(self):
        '''проверим можно ли собрать из этих сторон треугольник'''
        if self.a + self.b <= self.c or self.a + self.c <= self.b or self.b + self.c <= self.a:
            raise ValueError("Стороны не образуют треугольник!")

    def square(self) -> float:
        '''вычисляем площадь треугольника'''
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def is_right_triangle(self) -> bool:
        '''проверяет, является ли треугольник прямоугольным'''
        sides = sorted([self.a, self.b, self.c])
        return math.isclose(pow(sides[0], 2) + pow(sides[1], 2), pow(sides[2], 2))


def calculate_square(figure: Figure) -> float:
    '''Вычисление площади фигуры без знания типа фигуры'''
    return figure.square()
