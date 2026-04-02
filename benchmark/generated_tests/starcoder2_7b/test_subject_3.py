import unittest

class TestFactorial(unittest.TestCase):
    def test_factorial_0(self):
        self.assertEqual(factorial_(0), 1)

    def test_factorial_1(self):
        self.assertEqual(factorial_(1), 1)

    def test_factorial_2(self):
        self.assertEqual(factorial_(2), 2)

    def test_factorial_3(self):
        self.assertEqual(factorial_(3), 6)

    def test_factorial_4(self):
        self.assertEqual(factorial_(4), 24)

    def test_factorial_5(self):
        self.assertEqual(factorial_(5), 120)

if __name__ == '__main__':
    unittest.main()