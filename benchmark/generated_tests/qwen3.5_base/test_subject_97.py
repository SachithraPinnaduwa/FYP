import unittest

class TestEuclideanDistance(unittest.TestCase):
    def test_same_dimension(self):
        self.assertEqual(euclidean_distance((1, 2), (4, 6)), 3.0)
        self.assertEqual(euclidean_distance([1, 2], [4, 6]), 3.0)
        self.assertEqual(euclidean_distance((1, 2), [4, 6]), 3.0)
        self.assertEqual(euclidean_distance([1, 2], (4, 6)), 3.0)
    
    def test_invalid_input(self):
        self.assertEqual(euclidean_distance(1, 2), "Error: Inputs must be tuples or lists")
        self.assertEqual(euclidean_distance((1, 2), 2), "Error: Inputs must be tuples or lists")
        self.assertEqual(euclidean_distance((1, 2), [3, 4]), "Error: Both inputs should have the same dimension")
        self.assertEqual(euclidean_distance([1, 2], [3, 4, 5]), "Error: Both inputs should have the same dimension")
        self.assertEqual(euclidean_distance([1, 2], [3, 4, 5, 6]), "Error: Both inputs should have the same dimension")
        self.assertEqual(euclidean_distance([1, 2], [3, 4, 5, 6, 7]), "Error: Both inputs should have the same dimension")
        self.assertEqual(euclidean_distance([1, 2], [3, 4, 5, 6, 7, 8]), "Error: Both inputs should have the same dimension")
        self.assertEqual(euclidean_distance([1, 2], [3, 4, 5, 6, 7, 8, 9]), "Error: Both inputs should have the same dimension")
        self.assertEqual(euclidean_distance([1, 2], [3, 4, 5, 6, 7, 8, 9, 10]), "Error: Both inputs should have the same dimension")
        self.assertEqual(euclidean_distance([1, 2], [3, 4, 5, 6, 7, 8, 9, 10, 11]), "Error: Both inputs should have the same dimension")
        self.assertEqual(euclidean_distance([1, 2], [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]), "Error: Both inputs should have the same dimension")
        self.assertEqual(euclidean_distance([1, 2], [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]), "Error: Both inputs should have the same dimension")
        self.assertEqual(euclidean_distance([1, 2], [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]), "Error: Both inputs should have the same dimension")
        self.assertEqual(euclidean_distance([1, 2], [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), "Error: Both inputs should have the same dimension")
        self.assertEqual(euclidean_distance([1, 2], [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]), "Error: Both inputs should have the same dimension")
        self.assertEqual(euclidean_distance([1, 2], [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]), "Error: Both inputs should have the same dimension")
        self.assertEqual(euclidean_distance([1, 2], [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]), "Error: Both inputs should have the same dimension")
        self.assertEqual(euclidean_distance([1, 2], [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]), "Error: Both inputs should have the same dimension")
        self.assertEqual(euclidean_distance([1, 2], [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]), "Error: Both inputs should have the same dimension")
        self.assertEqual(euclidean_distance([1, 2], [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]), "Error: Both inputs should have the same dimension")
        self.assertEqual(euclidean_distance([1, 2], [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]), "Error: Both inputs should have the same dimension")
        self.assertEqual(euclidean_distance([1, 2], [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]), "Error: Both inputs should have the same dimension")
        self.assertEqual(euclidean_distance([1, 2], [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 1