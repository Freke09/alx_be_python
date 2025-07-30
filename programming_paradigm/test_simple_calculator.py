import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()


    def test_addition(self):
        self.assertEqual(self.calc.add(10, 5), 15)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-1, -1), -2)
    
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(4, 2), 2)
        self.assertEqual(self.calc.subtract(0, 2), -2)
    
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 5), 10)
        self.assertEqual(self.calc.multiply(-3, -3), 9)

    def test_divide(self):
        self.assertEqual(self.calc.divide(5, 2), 2.5)
        self.assertEqual(self.calc.divide(-4, 2), -2)
    
    def test_divide_by_zero(self):
        self.assertIsNone(self.calc.divide(10, 0))