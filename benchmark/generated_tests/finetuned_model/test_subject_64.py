import unittest

class TestGameOutcome(unittest.TestCase):

    def test_win_condition(self):
        # Test case for winning condition
        n = 5
        m = 6
        graph = {1: [2, 3], 2: [4, 5], 4: [], 5: []}
        start = 1
        expected_output = ("Win", [1, 2, 4, 5])
        self.assertEqual(determine_game_outcome(n, m, graph, start), expected_output)

    def test_lose_condition(self):
        # Test case for losing condition
        n = 3
        m = 2
        graph = {1: [3], 3: [], 2: [1]}
        start = 2
        expected_output = ("Lose", None)
        self.assertEqual(determine_game_outcome(n, m, graph, start), expected_output)

    def test_draw_condition(self):
        # Test case for draw condition
        n = 2
        m = 2
        graph = {1: [2], 2: [1]}
        start = 1
        expected_output = ("Draw", None)
        self.assertEqual(determine_game_outcome(n, m, graph, start), expected_output)

    def test_no_possible_moves(self):
        # Test case for no possible moves condition
        n = 1
        m = 0
        graph = {}
        start = 1
        expected_output = ("Lose", None)
        self.assertEqual(determine_game_outcome(n, m, graph, start), expected_output)

    def test_single_vertex(self):
        # Test case for single vertex graph
        n = 1
        m = 0
        graph = {1: []}
        start = 1
        expected_output = ("Lose", None)
        self.assertEqual(determine_game_outcome(n, m, graph, start), expected_output)

    def test_empty_graph(self):
        # Test case for empty graph
        n = 0
        m = 0
        graph = {}
        start = None
        expected_output = ("Lose", None)
        self.assertEqual(determine_game_outcome(n, m, graph, start), expected_output)

    def test_large_graph(self):
        # Test case for large graph
        n = 100000
        m = 100000
        graph = {i: [i + 1] for i in range(1, n)}
        graph[n] = []
        start = 1
        expected_output = ("Win", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99,