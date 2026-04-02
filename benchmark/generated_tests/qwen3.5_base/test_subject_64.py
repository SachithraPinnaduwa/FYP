import unittest

class TestDetermineGameOutcome(unittest.TestCase):
    def test_case_1(self):
        n = 3
        m = 3
        graph = {1: [2, 3], 2: [1, 3], 3: [1, 2]}
        start = 1
        result = determine_game_outcome(n, m, graph, start)
        self.assertEqual(result, ("Win", [1, 2, 3]))
    
    def test_case_2(self):
        n = 4
        m = 4
        graph = {1: [2, 3], 2: [1, 3, 4], 3: [1, 2, 4], 4: [2, 3]}
        start = 1
        result = determine_game_outcome(n, m, graph, start)
        self.assertEqual(result, ("Win", [1, 2, 3, 4]))
    
    def test_case_3(self):
        n = 5
        m = 5
        graph = {1: [2, 3, 4, 5], 2: [1, 3, 4, 5], 3: [1, 2, 4, 5], 4: [1, 2, 3, 5], 5: [1, 2, 3, 4]}
        start = 1
        result = determine_game_outcome(n, m, graph, start)
        self.assertEqual(result, ("Win", [1, 2, 3, 4, 5]))
    
    def test_case_4(self):
        n = 6
        m = 6
        graph = {1: [2, 3, 4, 5, 6], 2: [1, 3, 4, 5, 6], 3: [1, 2, 4, 5, 6], 4: [1, 2, 3, 5, 6], 5: [1, 2, 3, 4, 6], 6: [1, 2, 3, 4, 5]}
        start = 1
        result = determine_game_outcome(n, m, graph, start)
        self.assertEqual(result, ("Win", [1, 2, 3, 4, 5, 6]))
    
    def test_case_5(self):
        n = 7
        m = 7
        graph = {1: [2, 3, 4, 5, 6, 7], 2: [1, 3, 4, 5, 6, 7], 3: [1, 2, 4, 5, 6, 7], 4: [1, 2, 3, 5, 6, 7], 5: [1, 2, 3, 4, 6, 7], 6: [1, 2, 3, 4, 5, 7], 7: [1, 2, 3, 4, 5, 6]}
        start = 1
        result = determine_game_outcome(n, m, graph, start)
        self.assertEqual(result, ("Win", [1, 2, 3, 4, 5, 6, 7]))
    
    def test_case_6(self):
        n = 8
        m = 8
        graph = {1: [2, 3, 4, 5, 6, 7, 8], 2: [1, 3, 4, 5, 6, 7, 8], 3: [1, 2, 4, 5, 6, 7, 8], 4: [1, 2, 3, 5, 6, 7, 8], 5: [1, 2, 3, 4, 6, 7, 8], 6: [1, 2, 3, 4, 5, 7, 8], 7: [1, 2, 3, 4, 5, 6, 8], 8: [1, 2, 3, 4, 5, 6, 7]}
        start = 1
        result = determine_game_outcome(n, m, graph, start)
        self.assertEqual(result, ("Win", [1, 2, 3, 4, 5, 6, 7, 8]))
    
    def test_case_7(self):
        n = 9
        m = 9
        graph = {1: [2, 3, 4, 5, 6, 7, 8, 9], 2: [1, 3, 4, 5, 6, 7, 8, 9], 3: [1, 2, 4, 5, 6, 7, 8, 9], 4: [1, 2, 3, 5, 6, 7, 8, 9], 5: [1, 2, 3, 4, 6, 7, 8, 9], 6: [1, 2, 3, 4, 5, 7, 8, 9], 7: [1, 2, 3, 4, 5, 6, 8, 9], 8: [1, 2, 3, 4, 5, 6, 7, 9], 9: [1, 2, 3, 4, 5, 6, 7, 8]}
        start = 1
        result = determine_game_outcome(n, m, graph, start)
        self.assertEqual(result, ("Win", [1, 2, 3, 4, 5, 6, 7, 8, 9]))
    
    def test_case_8(self):
        n = 10
        m = 10
        graph = {1: [2, 3, 4, 5, 6, 7, 8, 9, 10], 2: [1, 3, 4, 5, 6, 7, 8, 9, 10], 3: [1, 2, 4, 5, 6, 7, 8, 9, 10], 4: [1, 2, 3, 5, 6, 7, 8, 9, 10], 5: [1, 2, 3, 4, 6