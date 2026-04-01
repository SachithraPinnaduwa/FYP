import unittest

class TestSudokuEngine(unittest.TestCase):
    def setUp(self):
        self.grid = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        self.engine = SudokuEngine(self.grid)

    def test_place_number_valid(self):
        self.assertTrue(self.engine.place_number(0, 0, 1))
        self.assertTrue(self.engine.place_number(0, 1, 2))
        self.assertTrue(self.engine.place_number(0, 2, 3))

    def test_place_number_invalid(self):
        self.grid[0][0] = 1
        self.assertFalse(self.engine.place_number(0, 0, 1))
        self.assertFalse(self.engine.place_number(0, 1, 1))

    def test_undo(self):
        self.engine.place_number(0, 0, 1)
        self.assertTrue(self.engine.undo())
        self.assertEqual(self.grid[0][0], 0)

    def test_undo_empty(self):
        self.assertFalse(self.engine.undo())

    def test_is_valid(self):
        self.assertTrue(self.engine._is_valid(0, 0, 1))
        self.assertFalse(self.engine._is_valid(0, 0, 1))

    def test_is_valid_row(self):
        self.grid[0] = [1, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertFalse(self.engine._is_valid(0, 1, 1))

    def test_is_valid_col(self):
        self.grid = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        self.grid[0][0] = 1
        self.assertFalse(self.engine._is_valid(1, 0, 1))

    def test_is_valid_box(self):
        self.grid = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        self.grid[0][0] = 1
        self.grid[1][1] = 1
        self.grid[2][2] = 1
        self.assertFalse(self.engine._is_valid(0, 0, 1))

if __name__ == '__main__':
    unittest.main()
