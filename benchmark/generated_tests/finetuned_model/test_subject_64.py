import unittest

class TestGameOutcome(unittest.TestCase):
    def test_case_1(self):
        n = 5
        m = 6
        graph = {
            1: [2, 3],
            2: [4, 5],
            3: [4],
            4: [5],
            5: []
        }
        start = 1
        expected_output = ("Win", [1, 2, 4, 5])
        self.assertEqual(determine_game_outcome(n, m, graph, start), expected_output)

    def test_case_2(self):
        n = 3
        m = 2
        graph = {
            1: [3],
            2: [1],
            3: []
        }
        start = 2
        expected_output = ("Lose", None)
        self.assertEqual(determine_game_outcome(n, m, graph, start), expected_output)

    def test_case_3(self):
        n = 2
        m = 2
        graph = {
            1: [2],
            2: [1]
        }
        start = 1
        expected_output = ("Draw", None)
        self.assertEqual(determine_game_outcome(n, m, graph, start), expected_output)

    def test_case_4(self):
        n = 4
        m = 5
        graph = {
            1: [2, 3],
            2: [4],
            3: [4],
            4: []
        }
        start = 1
        expected_output = ("Win", [1, 2, 4])
        self.assertEqual(determine_game_outcome(n, m, graph, start), expected_output)

    def test_case_5(self):
        n = 6
        m = 7
        graph = {
            1: [2],
            2: [3, 4],
            3: [5],
            4: [5],
            5: [6],
            6: []
        }
        start = 1
        expected_output = ("Win", [1, 2, 3, 5, 6])
        self.assertEqual(determine_game_outcome(n, m, graph, start), expected_output)

    def test_case_6(self):
        n = 5
        m = 5
        graph = {
            1: [2],
            2: [3, 4],
            3: [1],
            4: [1],
            5: []
        }
        start = 1
        expected_output = ("Draw", None)
        self.assertEqual(determine_game_outcome(n, m, graph, start), expected_output)

if __name__ == '__main__':
    unittest.main()