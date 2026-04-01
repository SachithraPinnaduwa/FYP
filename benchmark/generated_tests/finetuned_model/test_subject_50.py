import unittest

class TestDragRaceWinner(unittest.TestCase):

    def test_single_match(self):
        # Test case with a single match
        n = 1
        matches = ["a b"]
        self.assertEqual(find_drag_race_winner(n, matches), "a")

    def test_two_rounds(self):
        # Test case with two rounds
        n = 2
        matches = ["a b", "a c", "c d"]
        self.assertEqual(find_drag_race_winner(n, matches), "a")

    def test_multiple_rounds(self):
        # Test case with multiple rounds
        n = 3
        matches = ["a b", "c d", "e f", "a c", "a e", "b d", "b f", "a b"]
        self.assertEqual(find_drag_race_winner(n, matches), "a")

    def test_all_losers(self):
        # Test case where all racers are losers
        n = 1
        matches = ["a b", "b c"]
        self.assertIsNone(find_drag_race_winner(n, matches))

    def test_single_racer(self):
        # Test case with only one racer
        n = 0
        matches = []
        self.assertIsNone(find_drag_race_winner(n, matches))

    def test_large_number_of_rounds(self):
        # Test case with a large number of rounds
        n = 15
        matches = [f"{chr(97 + i)} {chr(98 + i)}" for i in range(2**n - 1)]
        self.assertIsNotNone(find_drag_race_winner(n, matches))