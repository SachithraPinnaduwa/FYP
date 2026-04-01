import unittest

class TestBinarySearch(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(binary_search([], 5), -1)

    def test_single_element_array_not_found(self):
        self.assertEqual(binary_search([3], 1), -1)

    def test_single_element_array_found(self):
        self.assertEqual(binary_search([3], 3), 0)

    def test_target_at_start(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 1), 0)

    def test_target_at_end(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 5), 4)

    def test_target_in_middle(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 3), 2)

    def test_target_before_first_element(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 0), -1)

    def test_target_after_last_element(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 6), -1)

    def test_duplicate_elements(self):
        self.assertEqual(binary_search([1, 2, 2, 2, 3, 4, 5], 2), 1)
        self.assertEqual(binary_search([1, 2, 2, 2, 3, 4, 5], 2), 2)
        self.assertEqual(binary_search([1, 2, 2, 2, 3, 4, 5], 2), 3)

if __name__ == '__main__':
    unittest.main()