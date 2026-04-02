from subject_97 import *

import unittest
import math

def euclidean_distance(point1, point2):
    if not isinstance(point1, (tuple, list)) or not isinstance(point2, (tuple, list)):
        return "Error: Inputs must be tuples or lists"
    if len(point1) != len(point2):
        return "Error: Both inputs should have the same dimension"
    
    distance = 0
    for i in range(len(point1)):
        distance += (point1[i] - point2[i]) ** 2
    
    return math.sqrt(distance)

class TestEuclideanDistance(unittest.TestCase):
    def test_valid_input(self):
        self.assertAlmostEqual(euclidean_distance((1, 2), (4, 6)), 5.0)
        self.assertAlmostEqual(euclidean_distance([1, 2, 3], [4, 5, 6]), 5.196152422706632)
    
    def test_different_dimensions(self):
        self.assertEqual(euclidean_distance((1, 2), (4, 6, 8)), "Error: Both inputs should have the same dimension")
    
    def test_non_numeric_input(self):
        self.assertEqual(euclidean_distance((1, 'a'), (4, 6)), "Error: Inputs must be tuples or lists")
    
    def test_single_dimension(self):
        self.assertAlmostEqual(euclidean_distance((1,), (4,)), 3.0)

if __name__ == '__main__':
    unittest.main()