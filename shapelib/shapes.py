import math
from abc import ABC, abstractmethod
from typing import Protocol


class Shape(ABC):
    """Базовый абстрактный класс для фигур."""

    @abstractmethod
    def area(self) -> float:
        """Вычислить площадь фигуры."""
        ...


class Circle(Shape):
    """Круг, задаётся радиусом."""

    def __init__(self, radius: float):
        if radius < 0:
            raise ValueError("Радиус не может быть отрицательным")
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2


class Triangle(Shape):
    """Треугольник по трём сторонам. Проверяет валидность и прямой угол."""

    def __init__(self, a: float, b: float, c: float):
        sides = sorted((a, b, c))
        if any(side <= 0 for side in sides):
            raise ValueError("Стороны должны быть положительными")
        if sides[0] + sides[1] <= sides[2]:
            raise ValueError("Треугольник с такими сторонами не существует")
        self.a, self.b, self.c = sides

    def area(self) -> float:
        # Герон
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def is_right(self, tol: float = 1e-9) -> bool:
        """Проверка прямого угла: a² + b² ≈ c²."""
        return abs(self.a**2 + self.b**2 - self.c**2) <= tol


# Пример добавления новой фигуры:
class Rectangle(Shape):
    """Прямоугольник по длине и ширине."""

    def __init__(self, width: float, height: float):
        if width < 0 or height < 0:
            raise ValueError("Стороны не могут быть отрицательными")
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height


# Утилита для динамического вычисления площади любой фигуры:
def compute_area(shape: Shape) -> float:
    """
    Вычисляет площадь, не зная конкретного типа фигуры на этапе компиляции.
    """
    return shape.area()
