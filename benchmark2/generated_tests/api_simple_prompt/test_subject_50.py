from subject_50 import *

import unittest

class TestDragRaceWinner(unittest.TestCase):
    def test_find_drag_race_winner(self):
        self.assertEqual(find_drag_race_winner(2, ["a b", "a c", "c d"]), "a")
        self.assertEqual(find_drag_race_winner(1, ["x y"]), "x")
        self.assertEqual(find_drag_race_winner(3, ["a b", "c d", "e f", "a c", "b d", "a e", "a f"]), "a")
        self.assertEqual(find_drag_race_winner(4, ["a b", "c d", "e f", "g h", "a c", "b d", "e g", "a e", "a f", "a h"]), "a")

if __name__ == '__main__':
    unittest.main()