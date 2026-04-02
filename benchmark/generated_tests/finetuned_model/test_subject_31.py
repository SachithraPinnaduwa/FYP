import unittest

class TestMinimumMoves(unittest.TestCase):
    def test_minimum_moves(self):
        self.assertEqual(minimum_moves(1, 2, 9, 8), 1)
        self.assertEqual(minimum_moves(5, 5, 5, 7), 2)
        self.assertEqual(minimum_moves(8, 6, 6, 8), 1)
        self.assertEqual(minimum_moves(3, 10, 8, 10), 2)
        self.assertEqual(minimum_moves(1, 1, 2, 2), 2)
        self.assertEqual(minimum_moves(1, 1, 3, 4), 1)
        self.assertEqual(minimum_moves(5, 5, 10, 10), 2)
        self.assertEqual(minimum_moves(2, 3, 1, 4), 2)
        self.assertEqual(minimum_moves(7, 7, 9, 1), 1)
        self.assertEqual(minimum_moves(4, 1, 8, 5), 2)

if __name__ == '__main__':
    unittest.main()