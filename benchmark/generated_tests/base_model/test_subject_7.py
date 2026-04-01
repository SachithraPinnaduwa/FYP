import unittest

class TestCountAndIndices(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(count_and_indices([], 5), (0, []))

    def test_target_not_in_array(self):
        self.assertEqual(count_and_indices([1, 3, 5, 7, 9], 4), (0, []))

    def test_single_occurrence(self):
        self.assertEqual(count_and_indices([1, 2, 3, 4, 5], 3), (1, [2]))

    def test_multiple_occurrences(self):
        self.assertEqual(count_and_indices([1, 2, 2, 2, 3, 4, 5], 2), (3, [1, 2, 3]))

    def test_all_elements_same(self):
        self.assertEqual(count_and_indices([1, 1, 1, 1, 1], 1), (5, [0, 1, 2, 3, 4]))

    def test_large_array(self):
        arr = list(range(1, 10**6))
        self.assertEqual(count_and_indices(arr, 500000), (1, [499999]))

    def test_boundary_values(self):
        self.assertEqual(count_and_indices([1, 10**9], 1), (1, [0]))
        self.assertEqual(count_and_indices([1, 10**9], 10**9), (1, [1]))

if __name__ == '__main__':
    unittest.main()