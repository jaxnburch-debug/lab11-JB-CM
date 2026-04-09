import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(sub(5, 3), 2)
        self.assertEqual(sub(0, 5), -5)
        self.assertEqual(sub(-2, -2), 0)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self):
        self.assertAlmostEqual(log(10, 100), 2)
        self.assertAlmostEqual(log(2, 8), 3)
        self.assertAlmostEqual(log(5, 25), 2)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            log(1, 10)

if __name__ == "__main__":
    unittest.main()