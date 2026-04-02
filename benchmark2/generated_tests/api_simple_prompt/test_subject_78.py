from subject_78 import *

import unittest

def factorial(n, acc=1):
    if n == 0:
        return acc
    else:
        return factorial(n - 1, acc * n)

class TestFactorial(unittest.TestCase):
    def test_factorial_0(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_1(self):
        self.assertEqual(factorial(1), 1)

    def test_factorial_2(self):
        self.assertEqual(factorial(2), 2)

    def test_factorial_3(self):
        self.assertEqual(factorial(3), 6)

    def test_factorial_4(self):
        self.assertEqual(factorial(4), 24)

    def test_factorial_5(self):
        self.assertEqual(factorial(5), 120)

    def test_factorial_10(self):
        self.assertEqual(factorial(10), 3628800)

    def test_factorial_20(self):
        self.assertEqual(factorial(20), 2432902008176640000)

if __name__ == '__main__':
    unittest.main()