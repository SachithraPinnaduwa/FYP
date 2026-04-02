import unittest

class TestFactorial(unittest.TestCase):
    """Test suite for the factorial function"""

    def test_factorial_0(self):
        """Test factorial of 0"""
        self.assertEqual(factorial_(0), 1)

    def test_factorial_1(self):
        """Test factorial of 1"""
        self.assertEqual(factorial_(1), 1)

    def test_factorial_5(self):
        """Test factorial of 5"""
        self.assertEqual(factorial_(5), 120)

    def test_factorial_10(self):
        """Test factorial of 10"""
        self.assertEqual(factorial_(10), 3628800)

    def test_factorial_negative(self):
        """Test factorial of negative number"""
        with self.assertRaises(ValueError):
            factorial_(-1)

    def test_factorial_large(self):
        """Test factorial of a large number"""
        self.assertEqual(factorial_(20), 2432902008176640000)

if __name__ == '__main__':
    unittest.main()
