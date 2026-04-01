import unittest

class TestFibonacciFunction(unittest.TestCase):

    def test_base_case_0(self):
        # Test the base case where n = 0
        self.assertEqual(entrance(0), 0)

    def test_base_case_1(self):
        # Test the base case where n = 1
        self.assertEqual(entrance(1), 1)

    def test_recursive_case_2(self):
        # Test the recursive case where n = 2
        self.assertEqual(entrance(2), 1)

    def test_recursive_case_3(self):
        # Test the recursive case where n = 3
        self.assertEqual(entrance(3), 2)

    def test_recursive_case_5(self):
        # Test the recursive case where n = 5
        self.assertEqual(entrance(5), 5)

    def test_recursive_case_10(self):
        # Test the recursive case where n = 10
        self.assertEqual(entrance(10), 55)

    def test_recursive_case_20(self):
        # Test the recursive case where n = 20
        self.assertEqual(entrance(20), 6765)

    def test_large_input(self):
        # Test a large input
        self.assertEqual(entrance(100), 354224848179261915075)