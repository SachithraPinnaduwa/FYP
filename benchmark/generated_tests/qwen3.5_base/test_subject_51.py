import unittest

class TestSumListRecursive(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(sum_list_recursive([]), 0)

    def test_single_element_list(self):
        self.assertEqual(sum_list_recursive([5]), 5)

    def test_two_element_list(self):
        self.assertEqual(sum_list_recursive([1, 2]), 3)

    def test_large_list(self):
        self.assertEqual(sum_list_recursive([1, 2, 3, 4, 5]), 15)

    def test_negative_numbers(self):
        self.assertEqual(sum_list_recursive([-1, -2, -3]), -6)

    def test_mixed_numbers(self):
        self.assertEqual(sum_list_recursive([1, -2, 3, -4, 5]), 3)

if __name__ == '__main__':
    unittest.main()
