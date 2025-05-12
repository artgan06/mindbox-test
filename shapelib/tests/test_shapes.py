import math
import pytest
from shapelib.shapes import Circle, Triangle, Rectangle, compute_area


def test_circle_area():
    c = Circle(2)
    assert math.isclose(c.area(), math.pi * 4)

    with pytest.raises(ValueError):
        Circle(-1)


def test_triangle_area_and_rightness():
    # простой треугольник 3-4-5
    t = Triangle(3, 4, 5)
    assert math.isclose(t.area(), 6.0)
    assert t.is_right()

    # не прямоугольный
    t2 = Triangle(2, 3, 4)
    assert not t2.is_right()

    with pytest.raises(ValueError):
        Triangle(1, 2, 3)  # вырожденный
    with pytest.raises(ValueError):
        Triangle(-1, 2, 2)  # отрицательная сторона


def test_rectangle_area():
    r = Rectangle(3, 5)
    assert r.area() == 15
    with pytest.raises(ValueError):
        Rectangle(-1, 2)


def test_compute_area_generic():
    shapes = [Circle(1), Triangle(3,4,5), Rectangle(2,3)]
    areas = [compute_area(s) for s in shapes]
    expected = [math.pi * 1**2, 6.0, 6.0]
    for got, exp in zip(areas, expected):
        assert math.isclose(got, exp)
