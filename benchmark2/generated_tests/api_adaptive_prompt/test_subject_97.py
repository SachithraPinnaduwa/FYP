from subject_97 import *

import unittest

class TestEuclideanDistance(unittest.TestCase):
    def test_normal_case_2d(self):
        self.assertAlmostEqual(euclidean_distance((1, 2), (4, 6)), 5.0)

    def test_normal_case_3d(self):
        self.assertAlmostEqual(euclidean_distance((1, 2, 3), (4, 5, 6)), 5.196152422706632)

    def test_edge_case_same_coordinates(self):
        self.assertEqual(euclidean_distance((0, 0), (0, 0)), 0.0)

    def test_error_handling_non_tuple_list_input(self):
        with self.assertRaisesRegex(ValueError, "Inputs must be tuples or lists"):
            euclidean_distance((1, 2), 'string')

    def test_error_handling_different_lengths(self):
        with self.assertRaisesRegex(ValueError, "Both inputs should have the same dimension"):
            euclidean_distance((1, 2), (3, 4, 5))

if __name__ == '__main__':
    unittest.main()