import unittest

class TestDragRaceWinner(unittest.TestCase):

    def test_single_round(self):
        n = 1
        matches = ["x y"]
        self.assertEqual(find_drag_race_winner(n, matches), "x")

    def test_two_rounds(self):
        n = 2
        matches = ["a b", "a c", "c d"]
        self.assertEqual(find_drag_race_winner(n, matches), "a")

    def test_three_rounds(self):
        n = 3
        matches = [
            "a b", "a c", "c d",
            "e f", "e g", "g h",
            "i j"
        ]
        self.assertEqual(find_drag_race_winner(n, matches), "a")

    def test_four_rounds(self):
        n = 4
        matches = [
            "a b", "a c", "c d", "d e",
            "f g", "f h", "h i", "i j",
            "k l", "k m", "m n", "n o",
            "p q", "p r", "r s", "s t"
        ]
        self.assertEqual(find_drag_race_winner(n, matches), "a")

    def test_all_wins_to_one_driver(self):
        n = 2
        matches = ["a b", "b c", "c a"]
        self.assertEqual(find_drag_race_winner(n, matches), "a")

    def test_tie_breaker_not_possible(self):
        n = 2
        matches = ["a b", "b a"]
        self.assertEqual(find_drag_race_winner(n, matches), "a")

    def test_large_input(self):
        n = 15
        matches = []
        current_char = 'a'
        for _ in range(2**n - 1):
            matches.append(f"{current_char} {chr(ord(current_char) + 1)}")
            current_char = chr(ord(current_char) + 2)
        self.assertEqual(find_drag_race_winner(n, matches), "a")

if __name__ == '__main__':
    unittest.main()