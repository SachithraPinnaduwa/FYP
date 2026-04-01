import unittest

class TicTacToeBoardTest(unittest.TestCase):
    def setUp(self):
        self.board = TicTacToeBoard()

    def test_initial_state(self):
        self.assertEqual(self.board.current_player, "X")
        self.assertEqual(self.board.winner, None)
        for row in self.board.board:
            for cell in row:
                self.assertEqual(cell, " ")

    def test_make_move_valid(self):
        self.assertTrue(self.board.make_move(0, 0))
        self.assertEqual(self.board.board[0][0], "X")
        self.assertEqual(self.board.current_player, "O")

    def test_make_move_invalid(self):
        self.assertFalse(self.board.make_move(0, 0))
        self.assertFalse(self.board.make_move(0, 0))

    def test_make_move_out_of_bounds(self):
        self.assertFalse(self.board.make_move(3, 0))
        self.assertFalse(self.board.make_move(0, 3))

    def test_make_move_winner(self):
        self.board.make_move(0, 0)
        self.board.make_move(1, 0)
        self.board.make_move(2, 0)
        self.assertEqual(self.board.winner, "X")
        self.assertFalse(self.board.make_move(0, 0))

    def test_make_move_draw(self):
        self.board.make_move(0, 0)
        self.board.make_move(0, 1)
        self.board.make_move(0, 2)
        self.board.make_move(1, 0)
        self.board.make_move(1, 1)
        self.board.make_move(1, 2)
        self.board.make_move(2, 0)
        self.board.make_move(2, 1)
        self.board.make_move(2, 2)
        self.assertEqual(self.board.winner, None)

    def test_make_move_diagonal_winner(self):
        self.board.make_move(0, 0)
        self.board.make_move(1, 1)
        self.board.make_move(2, 2)
        self.assertEqual(self.board.winner, "X")

    def test_make_move_anti_diagonal_winner(self):
        self.board.make_move(0, 2)
        self.board.make_move(1, 1)
        self.board.make_move(2, 0)
        self.assertEqual(self.board.winner, "X")

if __name__ == "__main__":
    unittest.main()
