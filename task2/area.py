from abc import ABC, abstractmethod
import math

e = 1e-6


class Figure(ABC):

    @abstractmethod
    def get_area(self):
        pass


class Triangle(Figure):

    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c

    def get_area(self) -> float:
        p = (self.a + self.b + self.c) / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5

    def is_right(self) -> bool:
        sides = [self.a, self.b, self.c]
        sides.sort()
        return abs(sides[0] ** 2 + sides[1] ** 2 - sides[2] ** 2) < e


class Circle(Figure):

    def __init__(self, r: float):
        self.r = r

    def get_area(self) -> float:
        return math.pi * self.r ** 2
