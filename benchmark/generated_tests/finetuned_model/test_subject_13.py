import unittest

class TestUniqueSortedArray(unittest.TestCase):
    def test_unique_sorted_array(self):
        self.assertEqual(unique_sorted_array([5, 3, 2, 4, 1, 3, 2, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(unique_sorted_array([-1, 0, 1, -1, 0, 1, -1, 0, 1]), [-1, 0, 1])
        self.assertEqual(unique_sorted_array([10, 20, 30, 40, 50]), [10, 20, 30, 40, 50])
        self.assertEqual(unique_sorted_array([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]), [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5])
        self.assertEqual(unique_sorted_array([7, 7, 7, 7, 7, 7, 7, 7]), [7])
        self.assertEqual(unique_sorted_array([]), [])

if __name__ == '__main__':
    unittest.main()