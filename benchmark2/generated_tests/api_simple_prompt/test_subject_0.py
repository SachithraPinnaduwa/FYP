from subject_0 import *

import unittest
import math

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    phi = (1 + math.sqrt(5)) / 2
    phi_n = phi ** n
    neg_phi_n = (-phi) ** (-n)
    
    return int((phi_n - neg_phi_n) / math.sqrt(5))

class TestFibonacci(unittest.TestCase):
    def test_fibonacci_0(self):
        self.assertEqual(fibonacci(0), 0)

    def test_fibonacci_1(self):
        self.assertEqual(fibonacci(1), 1)

    def test_fibonacci_2(self):
        self.assertEqual(fibonacci(2), 1)

    def test_fibonacci_3(self):
        self.assertEqual(fibonacci(3), 2)

    def test_fibonacci_4(self):
        self.assertEqual(fibonacci(4), 3)

    def test_fibonacci_5(self):
        self.assertEqual(fibonacci(5), 5)

    def test_fibonacci_10(self):
        self.assertEqual(fibonacci(10), 55)

    def test_fibonacci_20(self):
        self.assertEqual(fibonacci(20), 6765)

    def test_fibonacci_30(self):
        self.assertEqual(fibonacci(30), 832040)

    def test_fibonacci_40(self):
        self.assertEqual(fibonacci(40), 102334155)

    def test_fibonacci_50(self):
        self.assertEqual(fibonacci(50), 12586269025)

if __name__ == '__main__':
    unittest.main()