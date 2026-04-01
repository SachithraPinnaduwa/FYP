import unittest

class TestSolveFunction(unittest.TestCase):

    def test_empty_input(self):
        self.assertEqual(solve([]), [])

    def test_single_element(self):
        self.assertEqual(solve([5]), [5])

    def test_single_subarray(self):
        self.assertEqual(solve([[3, 1, 2]]), [[1, 2, 3]])

    def test_multiple_subarrays(self):
        self.assertEqual(solve([[4, 2], [1, 3]]), [[1, 3], [2, 4]])

    def test_mixed_elements(self):
        self.assertEqual(solve([[3, 1, 2], 5, [6, 4]]), [[1, 2, 3], [4, 6], 5])

    def test_already_sorted_subarrays(self):
        self.assertEqual(solve([[1, 2, 3], [4, 5, 6]]), [[1, 2, 3], [4, 5, 6]])

    def test_reverse_sorted_subarrays(self):
        self.assertEqual(solve([[3, 2, 1], [6, 5, 4]]), [[1, 2, 3], [4, 5, 6]])

    def test_subarrays_with_duplicates(self):
        self.assertEqual(solve([[3, 2, 2], [1, 1, 3]]), [[1, 1, 3], [2, 2, 3]])

    def test_normal_elements_with_duplicates(self):
        self.assertEqual(solve([3, 2, 2, 1, 1, 3]), [1, 1, 2, 2, 3, 3])

    def test_mixed_elements_with_duplicates(self):
        self.assertEqual(solve([[3, 2, 2], 1, 1, [6, 4]]), [[1, 1, 2, 2], [4, 6], 3])

if __name__ == '__main__':
    unittest.main()