import unittest

class TestKingMoves(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(count_king_moves(1, 3, 1), 6)

    def test_case_2(self):
        self.assertEqual(count_king_moves(2, 2, 2), 9)

    def test_case_3(self):
        self.assertEqual(count_king_moves(8, 8, 1), 1)

    def test_case_4(self):
        self.assertEqual(count_king_moves(1, 1, 1), 1)

    def test_case_5(self):
        self.assertEqual(count_king_moves(4, 4, 2), 13)

    def test_case_6(self):
        self.assertEqual(count_king_moves(8, 1, 1), 3)

    def test_case_7(self):
        self.assertEqual(count_king_moves(1, 8, 1), 3)

    def test_case_8(self):
        self.assertEqual(count_king_moves(5, 5, 3), 21)

if __name__ == '__main__':
    unittest.main()