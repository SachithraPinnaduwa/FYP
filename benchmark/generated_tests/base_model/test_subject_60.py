import unittest

class TestBinarySearch(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(binary_search([], 5), -1)

    def test_single_element_found(self):
        self.assertEqual(binary_search([3], 3), 0)
    
    def test_single_element_not_found(self):
        self.assertEqual(binary_search([3], 1), -1)

    def test_target_in_middle(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 3), 2)

    def test_target_at_start(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 1), 0)

    def test_target_at_end(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 5), 4)

    def test_large_array_with_target(self):
        self.assertEqual(binary_search(range(10000), 5000), 5000)

    def test_large_array_without_target(self):
        self.assertEqual(binary_search(range(10000), 10001), -1)

    def test_negative_numbers(self):
        self.assertEqual(binary_search([-5, -3, -1, 0, 2, 5], 0), 3)

    def test_repeated_elements(self):
        self.assertEqual(binary_search([1, 1, 2, 2, 2, 3, 4], 2), 2)

if __name__ == '__main__':
    unittest.main()