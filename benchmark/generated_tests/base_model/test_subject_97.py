import unittest
from math import sqrt

class TestEuclideanDistance(unittest.TestCase):

    def test_same_dimension_points(self):
        self.assertEqual(euclidean_distance((1, 2), (4, 6)), sqrt(17))
        self.assertEqual(euclidean_distance([3, 5], [1, 9]), sqrt(20))

    def test_different_dimension_points(self):
        self.assertEqual(euclidean_distance((1, 2, 3), (4, 6)), "Error: Both inputs should have the same dimension")
        self.assertEqual(euclidean_distance([3, 5, 7], [1, 9]), "Error: Both inputs should have the same dimension")

    def test_non_tuple_or_list_inputs(self):
        self.assertEqual(euclidean_distance("not a tuple", (4, 6)), "Error: Inputs must be tuples or lists")
        self.assertEqual(euclidean_distance((1, 2), "not a list"), "Error: Inputs must be tuples or lists")

    def test_empty_input(self):
        self.assertEqual(euclidean_distance([], []), "Error: Both inputs should have the same dimension")
        self.assertEqual(euclidean_distance((1, 2), ()), "Error: Both inputs should have the same dimension")

if __name__ == '__main__':
    unittest.main()