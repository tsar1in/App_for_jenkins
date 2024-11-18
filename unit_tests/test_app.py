import unittest
import allure
from app import app


@allure.feature('Юнит тест для подсчета корней квадратного уравнения')
class Test_roots_quadratic(unittest.TestCase):
    def setUp(self) -> None:
        self.equation = app.QuadraticEquationSolver(1, 2, 1)
    
    def test_calculate_discriminant(self) -> None:
        self.assertEqual(self.equation.calculate_discriminant(), 0.)

    def test_find_roots(self) -> None:
        self.assertEqual(self.equation.find_roots(1, 2, 1), (-1. , -1.))
        
if __name__ == "__main__":
    unittest.main()
