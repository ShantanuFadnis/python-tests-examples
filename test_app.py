import unittest
from app import fibonacci, factorial


class TestFibonacci(unittest.TestCase):
    def test_fibonacci_1(self):
        self.assertEqual(fibonacci(1), 1)

    def test_fibonacci_10(self):
        self.assertEqual(fibonacci(10), 55)


class TestFactorial(unittest.TestCase):
    def test_factorial_4(self):
        self.assertEqual(factorial(4), 24)
