from subject_17 import *

import unittest

def count_beautiful_fences(n: int, l: int, boards: list) -> int:
    MOD = 10 ** 9 + 7
    sze = 101
    
    dp = [[[0, 0] for _ in range(l + sze + 1)] for _ in range(n)]
    challengers = [[] for _ in range(sze)]
    
    for i in range(n):
        (a, b) = boards[i]
        if a != b:
            dp[i][a][1] = 1
            dp[i][b][0] = 1
        else:
            dp[i][a][1] = 1
        if a == b:
            challengers[a].append((a, i))
        else:
            challengers[a].append((b, i))
            challengers[b].append((a, i))
    
    for j in range(l + 1):
        for i in range(n):
            for z in range(2):
                if dp[i][j][z]:
                    for (a, ind) in challengers[boards[i][z]]:
                        if ind != i:
                            dp[ind][j + boards[i][z]][boards[ind].index(a)] = (dp[ind][j + boards[i][z]][boards[ind].index(a)] + dp[i][j][z]) % MOD
    
    cnt = 0
    for i in range(n):
        cnt = (cnt + dp[i][l][0] + dp[i][l][1]) % MOD
    
    return cnt

class TestCountBeautifulFences(unittest.TestCase):
    def test_normal_case_1(self):
        n = 2
        l = 3
        boards = [[1, 2], [2, 3]]
        expected = 2
        self.assertEqual(count_beautiful_fences(n, l, boards), expected)

    def test_normal_case_2(self):
        n = 1
        l = 2
        boards = [[2, 2]]
        expected = 1
        self.assertEqual(count_beautiful_fences(n, l, boards), expected)

    def test_normal_case_3(self):
        n = 6
        l = 6
        boards = [[2, 1], [3, 2], [2, 5], [3, 3], [5, 1], [2, 1]]
        expected = 20
        self.assertEqual(count_beautiful_fences(n, l, boards), expected)

    def test_edge_case_1(self):
        n = 2
        l = 0
        boards = [[1, 2], [2, 3]]
        expected = 1
        self.assertEqual(count_beautiful_fences(n, l, boards), expected)

    def test_edge_case_2(self):
        n = 1
        l = 3000
        boards = [[1, 1]]
        expected = 1
        self.assertEqual(count_beautiful_fences(n, l, boards), expected)

    def test_error_handling_1(self):
        n = 2
        l = -1
        boards = [[1, 2], [2, 3]]
        expected = 0
        self.assertEqual(count_beautiful_fences(n, l, boards), expected)

    def test_error_handling_2(self):
        n = 0
        l = 3
        boards = []
        expected = 0
        self.assertEqual(count_beautiful_fences(n, l, boards), expected)

if __name__ == '__main__':
    unittest.main()