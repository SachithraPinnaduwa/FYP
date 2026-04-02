from subject_61 import *

import unittest

def count_king_moves(R, C, K):
    # Calculate the range of rows and columns the king can move to
    a = min(8, R + K) - max(1, R - K) + 1
    b = min(8, C + K) - max(1, C - K) + 1
    
    # Return the total number of squares the king can visit
    return a * b

class TestCountKingMoves(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual(count_king_moves(4, 4, 1), 9)

    def test_edge_case_min_values(self):
        self.assertEqual(count_king_moves(1, 1, 1), 1)

    def test_edge_case_max_values(self):
        self.assertEqual(count_king_moves(8, 8, 8), 64)

    def test_error_handling(self):
        with self.assertRaises(ValueError):
            count_king_moves(0, 0, 0)

if __name__ == '__main__':
    unittest.main()