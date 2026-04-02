from subject_64 import *

import unittest

def determine_game_outcome(n, m, graph, start):
    mk = {}
    queue = [(start, 0, -1, 1)]
    cycle = False
    
    while len(queue) > 0:
        (v, player, prev, color) = queue.pop()
        if color == 2:
            mk[v, player] = (prev, 2)
            continue
        if mk.get((v, player), None):
            if mk[v, player][1] == 1:
                cycle = True
            continue
        mk[v, player] = (prev, 1)
        queue.append((v, player, prev, 2))
        for w in graph.get(v, []):
            queue.append((w, 1 - player, v, 1))
    
    sol = None
    for v in range(1, n + 1):
        if len(graph.get(v, [])) == 0 and mk.get((v, 1), None):
            sol = v
            break
    
    if sol:
        path = [sol]
        cur = (sol, 1)
        while cur != (start, 0):
            cur = (mk.get(cur)[0], 1 - cur[1])
            path.append(cur[0])
        return ("Win", path[::-1])
    elif cycle:
        return ("Draw", None)
    else:
        return ("Lose", None)

class TestDetermineGameOutcome(unittest.TestCase):
    def test_normal_case_win(self):
        n = 5
        m = 6
        graph = {1: [2, 3], 2: [4, 5], 3: [], 4: [], 5: []}
        start = 1
        expected = ('Win', [1, 2, 4, 5])
        self.assertEqual(determine_game_outcome(n, m, graph, start), expected)

    def test_normal_case_lose(self):
        n = 3
        m = 2
        graph = {1: [2], 2: [3], 3: []}
        start = 2
        expected = ('Lose', None)
        self.assertEqual(determine_game_outcome(n, m, graph, start), expected)

    def test_normal_case_draw(self):
        n = 2
        m = 2
        graph = {1: [2], 2: [1]}
        start = 1
        expected = ('Draw', None)
        self.assertEqual(determine_game_outcome(n, m, graph, start), expected)

    def test_edge_case_single_vertex(self):
        n = 1
        m = 0
        graph = {}
        start = 1
        expected = ('Draw', None)
        self.assertEqual(determine_game_outcome(n, m, graph, start), expected)

    def test_error_handling_invalid_start_vertex(self):
        n = 3
        m = 2
        graph = {1: [2], 2: [3], 3: []}
        start = 4
        expected = ('Lose', None)
        self.assertEqual(determine_game_outcome(n, m, graph, start), expected)

if __name__ == '__main__':
    unittest.main()