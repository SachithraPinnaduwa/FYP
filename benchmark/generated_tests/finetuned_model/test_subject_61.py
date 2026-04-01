import unittest

class TestKingMoves(unittest.TestCase):

    def test_base_case(self):
        # Test the base case where K is 0
        self.assertEqual(count_king_moves(1, 3, 0), 1)

    def test_small_K(self):
        # Test a small value of K
        self.assertEqual(count_king_moves(1, 3, 1), 6)

    def test_large_K(self):
        # Test a large value of K
        self.assertEqual(count_king_moves(1, 3, 8), 64)

    def test_edge_cases(self):
        # Test edge cases where R or C is at the edge of the board
        self.assertEqual(count_king_moves(1, 1, 1), 4)
        self.assertEqual(count_king_moves(1, 8, 1), 4)
        self.assertEqual(count_king_moves(8, 1, 1), 4)
        self.assertEqual(count_king_moves(8, 8, 1), 4)

    def test_king_in_center(self):
        # Test the case where the king is in the center of the board
        self.assertEqual(count_king_moves(4, 4, 1), 9)

    def test_king_at_corner(self):
        # Test the case where the king is at a corner of the board
        self.assertEqual(count_king_moves(1, 1, 1), 4)

    def test_king_at_edge(self):
        # Test the case where the king is at the edge of the board
        self.assertEqual(count_king_moves(1, 2, 1), 5)

    def test_king_at_middle(self):
        # Test the case where the king is at the middle of the board
        self.assertEqual(count_king_moves(5, 5, 1), 9)