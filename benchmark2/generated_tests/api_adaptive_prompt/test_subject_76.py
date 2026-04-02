from subject_76 import *

import unittest

def max_tower_height(n, rings):
    aux = [(float('inf'), 0, 0)]  # Initialize with a sentinel value
    for a, b, h in rings:
        aux.append((b, a, h))
    aux.sort(reverse=True)
    
    s = [0]
    p = [0] * (n + 1)
    
    for i in range(1, n + 1):
        while aux[s[-1]][1] >= aux[i][0]:
            s.pop()
        p[i] = p[s[-1]] + aux[i][2]
        s.append(i)
    
    return max(p)

class TestMaxTowerHeight(unittest.TestCase):
    def test_normal_case_1(self):
        n = 3
        rings = [(1, 5, 1), (2, 6, 2), (3, 7, 3)]
        expected = 6
        self.assertEqual(max_tower_height(n, rings), expected)

    def test_normal_case_2(self):
        n = 4
        rings = [(1, 2, 1), (1, 3, 3), (4, 6, 2), (5, 7, 1)]
        expected = 4
        self.assertEqual(max_tower_height(n, rings), expected)

    def test_edge_case_1(self):
        n = 1
        rings = [(2, 3, 1)]
        expected = 1
        self.assertEqual(max_tower_height(n, rings), expected)

    def test_edge_case_2(self):
        n = 100000
        rings = [(i, i+1, i) for i in range(1, 100001)]
        expected = 5000050000
        self.assertEqual(max_tower_height(n, rings), expected)

    def test_error_handling_1(self):
        n = 0
        rings = []
        expected = 0
        self.assertEqual(max_tower_height(n, rings), expected)

    def test_error_handling_2(self):
        n = 1
        rings = [(3, 3, 1)]
        expected = 0
        self.assertEqual(max_tower_height(n, rings), expected)

if __name__ == '__main__':
    unittest.main()