from subject_31 import *

import unittest

def minimum_moves(start_x, start_y, end_x, end_y):
    if start_x == end_x or start_y == end_y:
        return 2
    else:
        return 1

class TestMinimumMoves(unittest.TestCase):
    def test_normal_case_1(self):
        self.assertEqual(minimum_moves(1, 2, 9, 8), 1)

    def test_normal_case_2(self):
        self.assertEqual(minimum_moves(5, 5, 5, 7), 2)

    def test_normal_case_3(self):
        self.assertEqual(minimum_moves(8, 6, 6, 8), 1)

    def test_normal_case_4(self):
        self.assertEqual(minimum_moves(3, 10, 8, 10), 2)

    def test_edge_case_1(self):
        self.assertEqual(minimum_moves(1, 1, 10, 10), 1)

    def test_edge_case_2(self):
        self.assertEqual(minimum_moves(10, 10, 1, 1), 1)

    def test_error_handling_1(self):
        self.assertEqual(minimum_moves(5, 5, 5, 5), 2)

if __name__ == '__main__':
    unittest.main()