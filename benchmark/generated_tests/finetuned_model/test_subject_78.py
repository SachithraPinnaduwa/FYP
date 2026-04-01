import unittest

class TestFactorialFunction(unittest.TestCase):

    # Test case for the base case of 0
    def test_factorial_of_zero(self):
        self.assertEqual(factorial(0), 1)

    # Test case for the factorial of 1
    def test_factorial_of_one(self):
        self.assertEqual(factorial(1), 1)

    # Test case for the factorial of 5
    def test_factorial_of_five(self):
        self.assertEqual(factorial(5), 120)

    # Test case for the factorial of 10
    def test_factorial_of_ten(self):
        self.assertEqual(factorial(10), 3628800)

    # Test case for the factorial of a large number (100)
    def test_factorial_of_large_number(self):
        self.assertEqual(factorial(100), 9332621544394415268169923885626670049071596826438162146859296389521759999322991560894146397615651828625369792082722375825118521091686400000000000000000000000000000000000000000000000000000000)

    # Test case for the factorial of a negative number (should raise a ValueError)
    def test_factorial_of_negative_number(self):
        with self.assertRaises(ValueError):
            factorial(-1)