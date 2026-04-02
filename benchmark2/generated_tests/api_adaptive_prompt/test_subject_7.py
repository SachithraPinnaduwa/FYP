from subject_7 import *

import unittest

class TestCountAndIndices(unittest.TestCase):
    def test_count_and_indices(self):
        self.assertEqual(count_and_indices([1, 2, 2, 3, 4, 4, 4, 5], 2), (2, [1, 2]))
        self.assertEqual(count_and_indices([1, 1, 1, 1, 1, 1, 1, 1], 1), (8, [0, 1, 2, 3, 4, 5, 6, 7]))
        self.assertEqual(count_and_indices([1, 2, 3, 4, 5, 6, 7, 8], 9), (0, []))
        self.assertEqual(count_and_indices([1, 2, 3, 4, 5, 6, 7, 8], 1), (1, [0]))
        self.assertEqual(count_and_indices([1, 2, 3, 4, 5, 6, 7, 8], 8), (1, [7]))
        self.assertEqual(count_and_indices([1, 2, 3, 4, 5, 6, 7, 8], 4), (1, [3]))
        self.assertEqual(count_and_indices([1, 2, 3, 4, 5, 6, 7, 8], 5), (1, [4]))
        self.assertEqual(count_and_indices([1, 2, 3, 4, 5, 6, 7, 8], 6), (1, [5]))
        self.assertEqual(count_and_indices([1, 2, 3, 4, 5, 6, 7, 8], 7), (1, [6]))
        self.assertEqual(count_and_indices([1, 2, 3, 4, 5, 6, 7, 8], 8), (1, [7]))

if __name__ == '__main__':
    unittest.main()