import unittest

class TestMinIncrementOperations(unittest.TestCase):

    def test_base_case(self):
        # Test case with the base example from the problem statement
        arr = [1, 2, 2]
        N = len(arr)
        self.assertEqual(min_increment_operations(arr, N), 1)

    def test_example2(self):
        # Test case with the second example from the problem statement
        arr = [1, 1, 2, 3]
        N = len(arr)
        self.assertEqual(min_increment_operations(arr, N), 3)

    def test_all_unique(self):
        # Test case where all elements are unique
        arr = [1, 2, 3, 4, 5]
        N = len(arr)
        self.assertEqual(min_increment_operations(arr, N), 0)

    def test_all_equal(self):
        # Test case where all elements are the same
        arr = [5, 5, 5, 5, 5]
        N = len(arr)
        self.assertEqual(min_increment_operations(arr, N), 20)

    def test_empty_array(self):
        # Test case with an empty array
        arr = []
        N = len(arr)
        self.assertEqual(min_increment_operations(arr, N), 0)

    def test_single_element(self):
        # Test case with a single element
        arr = [1]
        N = len(arr)
        self.assertEqual(min_increment_operations(arr, N), 0)

    def test_large_array(self):
        # Test case with a large array
        arr = [i for i in range(100000)]
        N = len(arr)
        self.assertEqual(min_increment_operations(arr, N), 0)

    def test_array_with_duplicates(self):
        # Test case with a large array containing duplicates
        arr = [1] * 50000 + [2] * 50000
        N = len(arr)
        self.assertEqual(min_increment_operations(arr, N), 50000)