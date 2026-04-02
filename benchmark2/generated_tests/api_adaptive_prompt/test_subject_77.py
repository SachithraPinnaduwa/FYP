from subject_77 import *

import unittest

class TestMineGold(unittest.TestCase):
    def test_normal_case(self):
        goldMines = {'mine1': (10, 10), 'mine2': (30, 30), 'mine3': (50, 50)}
        centralHub = (20, 20)
        expected = (30, 40)
        self.assertEqual(mine_gold(goldMines, centralHub), expected)

    def test_edge_case_empty_gold_mines(self):
        goldMines = {}
        centralHub = (0, 0)
        expected = (0, 0)
        self.assertEqual(mine_gold(goldMines, centralHub), expected)

    def test_edge_case_all_mines_within_20_units(self):
        goldMines = {'mine1': (10, 10), 'mine2': (15, 15), 'mine3': (20, 20)}
        centralHub = (10, 10)
        expected = (0, 0)
        self.assertEqual(mine_gold(goldMines, centralHub), expected)

    def test_error_handling_invalid_input_types(self):
        goldMines = 'invalid'
        centralHub = 'invalid'
        with self.assertRaises(TypeError):
            mine_gold(goldMines, centralHub)

if __name__ == '__main__':
    unittest.main()