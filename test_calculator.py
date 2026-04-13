import unittest
from calculator import *
import math


class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(mul(2, 3), 6)
        self.assertEqual(mul(-1, 1), -1)
        self.assertEqual(mul(0, 5), 0)

    def test_divide(self):
        self.assertEqual(div(10, 2), 5)
        self.assertEqual(div(-6, 3), -2)
        self.assertEqual(div(0, 5), 0)

    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(3, 4), 5)
        self.assertAlmostEqual(hypotenuse(5, 12), 13)
        self.assertAlmostEqual(hypotenuse(8, 15), 17)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            math.log(-1, 10)

    def test_sqrt(self):
        self.assertEqual(math.sqrt(16), 4)
        self.assertEqual(math.sqrt(0), 0)
        with self.assertRaises(ValueError):
            math.sqrt(-1)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 5), -5)
        self.assertEqual(subtract(-2, -2), 0)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self):
        self.assertAlmostEqual(logarithm(10, 100), 2)
        self.assertAlmostEqual(logarithm(2, 8), 3)
        self.assertAlmostEqual(logarithm(5, 25), 2)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(1, 10)

if __name__ == "__main__":
    unittest.main()