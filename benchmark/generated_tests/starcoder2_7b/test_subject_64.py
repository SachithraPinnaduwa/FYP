import unittest

class Test(unittest.TestCase):
    def test_determine_game_outcome(self):
        self.assertEqual(determine_game_outcome(5, 6, {1: [2, 3], 2: [4, 5], 3: [4, 5], 4: [], 5: []}, 1), ("Win", [1, 2, 4, 5]))
        self.assertEqual(determine_game_outcome(3, 2, {1: [3], 2: [1], 3: []}, 2), ("Lose", None))
        self.assertEqual(determine_game_outcome(2, 2, {1: [2], 2: [1]}, 1), ("Draw", None))

if __name__ == '__main__':
    unittest.main()