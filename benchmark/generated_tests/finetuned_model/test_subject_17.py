import unittest

class TestBeautifulFences(unittest.TestCase):

    def test_base_case(self):
        # Test the base case where there is only one type of board and the fence length is the same as the board length
        n = 1
        l = 2
        boards = [(2, 2)]
        self.assertEqual(count_beautiful_fences(n, l, boards), 1)

    def test_two_types_of_boards(self):
        # Test the case where there are two types of boards and the fence length is the sum of the board lengths
        n = 2
        l = 3
        boards = [(1, 2), (2, 3)]
        self.assertEqual(count_beautiful_fences(n, l, boards), 2)

    def test_multiple_types_of_boards(self):
        # Test the case where there are multiple types of boards and the fence length is greater than the sum of the board lengths
        n = 6
        l = 6
        boards = [(2, 1), (3, 2), (2, 5), (3, 3), (5, 1), (2, 1)]
        self.assertEqual(count_beautiful_fences(n, l, boards), 20)

    def test_large_fence_length(self):
        # Test the case where the fence length is large
        n = 100
        l = 3000
        boards = [(1, 1)] * n
        self.assertEqual(count_beautiful_fences(n, l, boards), n * n)

    def test_no_challengers(self):
        # Test the case where there are no challengers
        n = 1
        l = 1
        boards = [(1, 1)]
        self.assertEqual(count_beautiful_fences(n, l, boards), 1)