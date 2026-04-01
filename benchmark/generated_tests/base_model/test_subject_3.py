import unittest

class TestFactorial(unittest.TestCase):

    def test_base_case_zero(self):
        self.assertEqual(factorial_(0), 1)

    def test_base_case_one(self):
        self.assertEqual(factorial_(1), 1)

    def test_factorial_two(self):
        self.assertEqual(factorial_(2), 2)

    def test_factorial_three(self):
        self.assertEqual(factorial_(3), 6)

    def test_factorial_four(self):
        self.assertEqual(factorial_(4), 24)

    def test_factorial_five(self):
        self.assertEqual(factorial_(5), 120)

    def test_factorial_ten(self):
        self.assertEqual(factorial_(10), 3628800)

if __name__ == '__main__':
    unittest.main()