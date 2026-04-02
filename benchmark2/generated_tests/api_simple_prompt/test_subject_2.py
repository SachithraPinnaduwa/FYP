from subject_2 import *

import unittest

def bottom_up_cut_rod(p, n):
    """
    Returns a tuple containing the maximum possible revenue and the lengths of the pieces 
    that make up the optimal solution for a rod of length n and price array p.

    Args:
    p (list): A list of length n+1 representing the prices of rods of different lengths.
    n (int): The length of the rod.

    Returns:
    tuple: A tuple containing the maximum revenue and the lengths of the pieces.
    """
    r = [0 for _ in range(n + 1)]
    s = [0 for _ in range(n + 1)]
    for j in range(1, n + 1):
        q = -1
        for i in range(1, j + 1):
            if q < p[i] + r[j - i]:
                q = p[i] + r[j - i]
                s[j] = i
        r[j] = q
    cut_sizes = []
    while n > 0:
        cut_sizes.append(s[n])
        n = n - s[n]
    return r[-1], cut_sizes

class TestBottomUpCutRod(unittest.TestCase):
    def test_case_1(self):
        p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
        n = 10
        expected_revenue = 30
        expected_cut_sizes = [10]
        self.assertEqual(bottom_up_cut_rod(p, n), (expected_revenue, expected_cut_sizes))

    def test_case_2(self):
        p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 26]
        n = 10
        expected_revenue = 31
        expected_cut_sizes = [1, 10]
        self.assertEqual(bottom_up_cut_rod(p, n), (expected_revenue, expected_cut_sizes))

    def test_case_3(self):
        p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 26]
        n = 11
        expected_revenue = 31
        expected_cut_sizes = [1, 10]
        self.assertEqual(bottom_up_cut_rod(p, n), (expected_revenue, expected_cut_sizes))

    def test_case_4(self):
        p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 26]
        n = 12
        expected_revenue = 35
        expected_cut_sizes = [2, 10]
        self.assertEqual(bottom_up_cut_rod(p, n), (expected_revenue, expected_cut_sizes))

    def test_case_5(self):
        p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 26]
        n = 13
        expected_revenue = 35
        expected_cut_sizes = [2, 10]
        self.assertEqual(bottom_up_cut_rod(p, n), (expected_revenue, expected_cut_sizes))

if __name__ == '__main__':
    unittest.main()