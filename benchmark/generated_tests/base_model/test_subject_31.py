import unittest

class TestMinimumMoves(unittest.TestCase):
    def test_minimum_moves(self):
        self.assertEqual(minimum_moves(1, 2, 9, 8), 1)
        self.assertEqual(minimum_moves(5, 5, 5, 7), 2)
        self.assertEqual(minimum_moves(8, 6, 6, 8), 1)
        self.assertEqual(minimum_moves(3, 10, 8, 10), 2)

if __name__ == '__main__':
    unittest.main()