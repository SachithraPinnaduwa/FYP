import unittest

class TestSumEven(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(sum_even([]), 0)

    def test_single_even(self):
        self.assertEqual(sum_even([2]), 2)

    def test_single_odd(self):
        self.assertEqual(sum_even([1]), 0)

    def test_mixed(self):
        self.assertEqual(sum_even([1, 2, 3, 4]), 6)

    def test_all_even(self):
        self.assertEqual(sum_even([2, 4, 6]), 12)

    def test_all_odd(self):
        self.assertEqual(sum_even([1, 3, 5]), 0)

    def test_large_list(self):
        self.assertEqual(sum_even(list(range(1, 101))), 2550)

if __name__ == '__main__':
    unittest.main()
