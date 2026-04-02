from subject_64 import *

import unittest

class TestGameOutcome(unittest.TestCase):
    def test_case_1(self):
        n = 5
        m = 6
        graph = {
            1: {2, 3},
            2: {4, 5},
            3: {4},
            4: {5},
            5: set()
        }
        start = 1
        expected = ("Win", [1, 2, 4, 5])
        self.assertEqual(determine_game_outcome(n, m, graph, start), expected)

    def test_case_2(self):
        n = 3
        m = 2
        graph = {
            1: {3},
            2: {1},
            3: set()
        }
        start = 2
        expected = ("Lose", None)
        self.assertEqual(determine_game_outcome(n, m, graph, start), expected)

    def test_case_3(self):
        n = 2
        m = 2
        graph = {
            1: {2},
            2: {1}
        }
        start = 1
        expected = ("Draw", None)
        self.assertEqual(determine_game_outcome(n, m, graph, start), expected)

if __name__ == '__main__':
    unittest.main()