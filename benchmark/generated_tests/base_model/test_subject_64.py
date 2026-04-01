import unittest

class TestGameOutcome(unittest.TestCase):

    def test_win_condition(self):
        self.assertEqual(determine_game_outcome(5, 6, {1: [2, 3], 2: [4, 5], 3: [4], 4: [], 5: []}, 1), 
                         ('Win', [1, 2, 4, 5]))

    def test_lose_condition(self):
        self.assertEqual(determine_game_outcome(3, 2, {1: [3], 2: [1], 3: []}, 2), 
                         ('Lose', None))

    def test_draw_condition(self):
        self.assertEqual(determine_game_outcome(2, 2, {1: [2], 2: [1]}, 1), 
                         ('Draw', None))

    def test_no_moves_for_vasya(self):
        self.assertEqual(determine_game_outcome(4, 3, {1: [2], 2: [3], 3: [4], 4: []}, 1), 
                         ('Win', [1, 2, 3, 4]))

    def test_cycle_and_draw(self):
        self.assertEqual(determine_game_outcome(3, 3, {1: [2], 2: [3], 3: [1]}, 1), 
                         ('Draw', None))

    def test_single_vertex_graph(self):
        self.assertEqual(determine_game_outcome(1, 0, {}, 1), 
                         ('Draw', None))

    def test_large_number_of_edges(self):
        graph = {i: [i+1] for i in range(1, 100000)}
        self.assertEqual(determine_game_outcome(100000, 99999, graph, 1), 
                         ('Win', list(range(1, 100001))))

if __name__ == '__main__':
    unittest.main()