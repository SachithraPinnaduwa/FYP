import unittest

class TestEuclideanDistanceFunction(unittest.TestCase):

    def test_same_length_points(self):
        # Test case with two points of the same length
        point1 = (1, 2, 3)
        point2 = (4, 5, 6)
        self.assertAlmostEqual(euclidean_distance(point1, point2), 5.196152422706632, places=6)

    def test_different_length_points(self):
        # Test case with two points of different lengths
        point1 = (1, 2, 3)
        point2 = (4, 5)
        self.assertEqual(euclidean_distance(point1, point2), "Error: Both inputs should have the same dimension")

    def test_input_not_tuple_or_list(self):
        # Test case with inputs that are not tuples or lists
        point1 = (1, 2, 3)
        point2 = 'not a tuple or list'
        self.assertEqual(euclidean_distance(point1, point2), "Error: Inputs must be tuples or lists")

    def test_zero_dimensional_points(self):
        # Test case with zero-dimensional points
        point1 = ()
        point2 = ()
        self.assertEqual(euclidean_distance(point1, point2), "Error: Both inputs should have the same dimension")

    def test_single_dimensional_points(self):
        # Test case with single-dimensional points
        point1 = (1,)
        point2 = (2,)
        self.assertAlmostEqual(euclidean_distance(point1, point2), 1.0, places=6)

    def test_negative_coordinates(self):
        # Test case with negative coordinates
        point1 = (-1, -2, -3)
        point2 = (4, 5, 6)
        self.assertAlmostEqual(euclidean_distance(point1, point2), 15.588457268119896, places=6)

    def test_large_coordinates(self):
        # Test case with large coordinates
        point1 = (1000000, 2000000, 3000000)
        point2 = (4000000, 5000000, 6000000)
        self.assertAlmostEqual(euclidean_distance(point1, point2), 5000000.0, places=6)