import unittest

class TestFactorialFunction(unittest.TestCase):
    def test_factorial_of_0(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_of_1(self):
        self.assertEqual(factorial(1), 1)

    def test_factorial_of_5(self):
        self.assertEqual(factorial(5), 120)

    def test_factorial_of_10(self):
        self.assertEqual(factorial(10), 3628800)

    def test_factorial_of_large_number(self):
        self.assertEqual(factorial(20), 2432902008176640000)

if __name__ == '__main__':
    unittest.main()