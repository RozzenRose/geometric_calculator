import unittest
import math
from geometric_calculator.figures import Circle, Triangle, calculate_square, Figure


class TestCircle(unittest.TestCase):

    def test_circle_square(self):
        '''тест метода вычисления площади через радиус'''
        circle = Circle(2)
        expected = math.pi * 4
        self.assertAlmostEqual(circle.square(), expected, places=5)

    def test_calculate_square_with_circle(self):
        '''тест метода нахождения площади любой фигуры, при передаче окружности'''
        circle = Circle(3)
        expected = math.pi * 9
        self.assertAlmostEqual(calculate_square(circle), expected, places=5)


class TestTriangle(unittest.TestCase):

    def test_triangle_square(self):
        '''тест метода нахождения площади треугольника по трем сторонам'''
        triangle = Triangle(3, 4, 5)
        expected = 6.0
        self.assertAlmostEqual(triangle.square(), expected, places=5)

    def test_invalid_triangle(self):
        '''тест метода валидации триугольника по трем сторонам'''
        with self.assertRaises(ValueError):
            Triangle(1, 2, 10)  # такие стороны не образуют треугольник

    def test_is_right_triangle_true(self):
        '''тест метода определение прямоугольности треугольника, когда треугольник прямоугольный'''
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.is_right_triangle())

    def test_is_right_triangle_false(self):
        '''тест метода определение прямоугольности треугольника, когда треугольник не прямоугольный'''
        triangle = Triangle(3, 4, 6)
        self.assertFalse(triangle.is_right_triangle())

    def test_calculate_square_with_triangle(self):
        '''тест метода нахождения площади любой фигуры, при передаче трeугольника'''
        triangle = Triangle(6, 8, 10)
        expected = 24.0
        self.assertAlmostEqual(calculate_square(triangle), expected, places=5)


class TestAbstractFigure(unittest.TestCase):

    def test_abstract_class_cannot_be_instantiated(self):
        with self.assertRaises(TypeError):
            '''проверяем невозможность создать экземпляр абстрактного класса'''
            Figure()


