import math
import os

class GeometricShape:
    """Базовий клас Фігура відповідно до специфікації завдання"""
    def dimention(self):
        raise NotImplementedError()

    def perimetr(self):
        raise AttributeError("Цей метод не підтримується для даного типу фігури")

    def square(self):
        raise AttributeError("Цей метод не підтримується для даного типу фігури")

    def squareSurface(self):
        raise AttributeError("Цей метод не підтримується для даного типу фігури")

    def squareBase(self):
        raise AttributeError("Цей метод не підтримується для даного типу фігури")

    def height(self):
        raise AttributeError("Цей метод не підтримується для даного типу фігури")

    def volume(self):
        raise NotImplementedError()


class Triangle(GeometricShape):
    def __init__(self, side_a, side_b, side_c):
        self.side_a, self.side_b, self.side_c = float(side_a), float(side_b), float(side_c)
        if self.side_a <= 0 or self.side_b <= 0 or self.side_c <= 0:
            raise ValueError("Сторони повинні бути більшими за нуль")
        if self.side_a + self.side_b <= self.side_c or self.side_a + self.side_c <= self.side_b or self.side_b + self.side_c <= self.side_a:
            raise ValueError("Неіснуючий трикутник")

    def dimention(self):
        return 2

    def perimetr(self):
        return self.side_a + self.side_b + self.side_c

    def square(self):
        half_p = self.perimetr() * 0.5
        return math.sqrt(half_p * (half_p - self.side_a) * (half_p - self.side_b) * (half_p - self.side_c))

    def volume(self):
        return self.square()


class Rectangle(GeometricShape):
    def __init__(self, width, height_val):
        self.width, self.height_val = float(width), float(height_val)
        if self.width <= 0 or self.height_val <= 0:
            raise ValueError("Сторони повинні бути більшими за нуль")

    def dimention(self):
        return 2

    def perimetr(self):
        return 2 * (self.width + self.height_val)

    def square(self):
        return self.width * self.height_val

    def volume(self):
        return self.square()


class Circle(GeometricShape):
    def __init__(self, radius):
        self.radius = float(radius)
        if self.radius <= 0:
            raise ValueError("Радіус повинен бути більшим за нуль")

    def dimention(self):
        return 2

    def perimetr(self):
        return 2 * math.pi * self.radius

    def square(self):
        return math.pi * (self.radius ** 2)

    def volume(self):
        return self.square()


class Ball(GeometricShape):
    def __init__(self, radius):
        self.radius = float(radius)
        if self.radius <= 0:
            raise ValueError("Радіус повинен бути більшим за нуль")

    def dimention(self):
        return 3

    def squareSurface(self):
        return 4 * math.pi * (self.radius ** 2)

    def volume(self):
        return (4 / 3) * math.pi * (self.radius ** 3)


class Parallelogram(GeometricShape):
    def __init__(self, side_a, side_b, h):
        self.side_a, self.side_b, self.h = float(side_a), float(side_b), float(h)
        if self.side_a <= 0 or self.side_b <= 0 or self.h <= 0:
            raise ValueError("Параметри повинні бути більшими за нуль")

    def dimention(self):
        return 2

    def perimetr(self):
        return 2 * (self.side_a + self.side_b)

    def square(self):
        return self.side_a * self.h

    def volume(self):
        return self.square()


class Trapeze(GeometricShape):
    def __init__(self, base_1, base_2, side_1, side_2):
        self.base_1, self.base_2 = float(base_1), float(base_2)
        self.side_1, self.side_2 = float(side_1), float(side_2)
        if self.base_1 <= 0 or self.base_2 <= 0 or self.side_1 <= 0 or self.side_2 <= 0 or self.base_1 == self.base_2:
            raise ValueError("Некоректні параметри трапеції")

    def dimention(self):
        return 2

    def perimetr(self):
        return self.base_1 + self.base_2 + self.side_1 + self.side_2

    def square(self):
        delta = abs(self.base_1 - self.base_2)
        fraction = (self.side_1 ** 2 + delta ** 2 - self.side_2 ** 2) / (2 * delta)
        h_sq = self.side_1 ** 2 - fraction ** 2
        if h_sq <= 0:
            raise ValueError("Геометрично неможлива трапеція")
        return ((self.base_1 + self.base_2) / 2) * math.sqrt(h_sq)

    def volume(self):
        return self.square()


class TriangularPyramid(Triangle):
    def __init__(self, base_side, height_val):
        super().__init__(base_side, base_side, base_side)
        self.h = float(height_val)
        if self.h <= 0:
            raise ValueError("Висота повинна бути більшою за нуль")

    def dimention(self):
        return 3

    def height(self):
        return self.h

    def squareBase(self):
        return super().square()

    def squareSurface(self):
        radius_in = self.squareBase() / (0.5 * super().perimetr())
        apothem = math.sqrt(self.h ** 2 + radius_in ** 2)
        return 0.5 * super().perimetr() * apothem