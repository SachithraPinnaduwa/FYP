import unittest

class TestBinarySearch(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(binary_search([], 5), -1)

    def test_single_element_array(self):
        self.assertEqual(binary_search([5], 5), 0)
        self.assertEqual(binary_search([5], 10), -1)

    def test_sorted_array(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 3), 2)
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 1), 0)
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 5), 4)

    def test_array_with_duplicates(self):
        self.assertEqual(binary_search([1, 2, 2, 3, 4, 5], 2), 1)
        self.assertEqual(binary_search([1, 2, 2, 3, 4, 5], 3), 3)
        self.assertEqual(binary_search([1, 2, 2, 3, 4, 5], 5), 5)

    def test_target_not_in_array(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 0), -1)
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 6), -1)

if __name__ == '__main__':
    unittest.main()