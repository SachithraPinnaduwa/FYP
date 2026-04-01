import unittest

class TestMineGoldFunction(unittest.TestCase):

    def test_single_mine(self):
        # Test with a single gold mine that is far enough from the central hub
        goldMines = {'mine1': (30, 30)}
        centralHub = (10, 10)
        expected_output = (10, math.sqrt((30-10)**2 + (30-10)**2))
        self.assertEqual(mine_gold(goldMines, centralHub), expected_output)

    def test_multiple_mines(self):
        # Test with multiple gold mines that are far enough from the central hub
        goldMines = {'mine1': (30, 30), 'mine2': (40, 40), 'mine3': (50, 50)}
        centralHub = (10, 10)
        expected_output = (30, 3 * math.sqrt((30-10)**2 + (30-10)**2))
        self.assertEqual(mine_gold(goldMines, centralHub), expected_output)

    def test_mine_too_close(self):
        # Test with a gold mine that is too close to the central hub
        goldMines = {'mine1': (20, 20)}
        centralHub = (10, 10)
        expected_output = (0, 0)
        self.assertEqual(mine_gold(goldMines, centralHub), expected_output)

    def test_no_mines(self):
        # Test with no gold mines
        goldMines = {}
        centralHub = (10, 10)
        expected_output = (0, 0)
        self.assertEqual(mine_gold(goldMines, centralHub), expected_output)

    def test_central_hub_at_origin(self):
        # Test with the central hub at the origin
        goldMines = {'mine1': (30, 0), 'mine2': (0, 30)}
        centralHub = (0, 0)
        expected_output = (20, 30)
        self.assertEqual(mine_gold(goldMines, centralHub), expected_output)

    def test_mines_on_the_same_line(self):
        # Test with gold mines on the same line
        goldMines = {'mine1': (20, 0), 'mine2': (40, 0)}
        centralHub = (10, 0)
        expected_output = (20, 2 * 20)
        self.assertEqual(mine_gold(goldMines, centralHub), expected_output)