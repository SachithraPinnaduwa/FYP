from subject_7 import *

import unittest

class TestCountAndIndices(unittest.TestCase):
    def test_count_and_indices(self):
        self.assertEqual(count_and_indices([1, 2, 4, 4, 4, 5, 6], 4), (3, [2, 3, 4]))
        self.assertEqual(count_and_indices([1, 1, 1, 1, 1, 1, 1], 1), (7, [0, 1, 2, 3, 4, 5, 6]))
        self.assertEqual(count_and_indices([2, 3, 5, 7, 11, 13, 17], 10), (0, []))
        self.assertEqual(count_and_indices([10, 20, 30, 40, 50], 25), (0, []))
        self.assertEqual(count_and_indices([1, 3, 5, 7, 9], 1), (1, [0]))
        self.assertEqual(count_and_indices([1, 3, 5, 7, 9], 9), (1, [4]))

if __name__ == '__main__':
    unittest.main()