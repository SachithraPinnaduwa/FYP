import unittest

class TestKingMoves(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(count_king_moves(1, 3, 1), 6)

    def test_case_2(self):
        self.assertEqual(count_king_moves(4, 4, 2), 17)

    def test_case_3(self):
        self.assertEqual(count_king_moves(8, 1, 3), 16)

    def test_case_4(self):
        self.assertEqual(count_king_moves(1, 1, 1), 6)

    def test_case_5(self):
        self.assertEqual(count_king_moves(8, 8, 1), 6)

    def test_case_6(self):
        self.assertEqual(count_king_moves(5, 5, 0), 1)

    def test_case_7(self):
        self.assertEqual(count_king_moves(2, 3, 2), 13)

    def test_case_8(self):
        self.assertEqual(count_king_moves(4, 6, 3), 25)

    def test_case_9(self):
        self.assertEqual(count_king_moves(1, 8, 2), 13)

    def test_case_10(self):
        self.assertEqual(count_king_moves(8, 1, 2), 13)

if __name__ == '__main__':
    unittest.main()