import unittest
import math

class TestFibonacci(unittest.TestCase):

    def test_base_cases(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)

    def test_small_values(self):
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(3), 2)
        self.assertEqual(fibonacci(4), 3)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(6), 8)

    def test_large_values(self):
        self.assertEqual(fibonacci(10), 55)
        self.assertEqual(fibonacci(20), 6765)
        self.assertEqual(fibonacci(30), 832040)
        self.assertEqual(fibonacci(40), 102334155)
        self.assertEqual(fibonacci(50), 12586269025)

    def test_negative_values(self):
        with self.assertRaises(ValueError):
            fibonacci(-1)
        with self.assertRaises(ValueError):
            fibonacci(-10)

    def test_non_integer_values(self):
        with self.assertRaises(TypeError):
            fibonacci('a')
        with self.assertRaises(TypeError):
            fibonacci(3.14)

if __name__ == '__main__':
    unittest.main()