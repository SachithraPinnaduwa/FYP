from subject_88 import *

import unittest

def find_min_deviation_shift(n, p):
    res = 0
    ires = 0
    neg = 0
    when = [0] * n
    
    # Transform the permutation to calculate initial deviation
    for i in range(n):
        p[i] = i + 1 - p[i]
        res += abs(p[i])
        if p[i] <= 0:
            neg += 1
        a = -p[i]
        if a < 0:
            a = a + n
        when[a] += 1
    
    ares = res
    
    # Calculate the deviation for each cyclic shift
    for i in range(n):
        neg -= when[i]
        ares -= neg
        ares += n - neg
        x = p[n - i - 1] + i + 1
        ares -= x
        ares += n - x
        neg += 1
        if ares < res:
            res = ares
            ires = i + 1
    
    return res, ires

class TestFindMinDeviationShift(unittest.TestCase):
    def test_normal_case_1(self):
        n = 3
        p = [1, 2, 3]
        expected = (0, 0)
        self.assertEqual(find_min_deviation_shift(n, p), expected)

    def test_normal_case_2(self):
        n = 3
        p = [2, 3, 1]
        expected = (0, 1)
        self.assertEqual(find_min_deviation_shift(n, p), expected)

    def test_normal_case_3(self):
        n = 3
        p = [3, 2, 1]
        expected = (2, 1)
        self.assertEqual(find_min_deviation_shift(n, p), expected)

    def test_edge_case_1(self):
        n = 2
        p = [1, 2]
        expected = (0, 0)
        self.assertEqual(find_min_deviation_shift(n, p), expected)

    def test_edge_case_2(self):
        n = 1000000
        p = [i for i in range(1, 1000001)]
        expected = (0, 0)
        self.assertEqual(find_min_deviation_shift(n, p), expected)

    def test_error_handling_1(self):
        n = 3
        p = [1, 2, 4]
        with self.assertRaises(Exception):
            find_min_deviation_shift(n, p)

    def test_error_handling_2(self):
        n = 3
        p = [1, 2, 2]
        with self.assertRaises(Exception):
            find_min_deviation_shift(n, p)

if __name__ == '__main__':
    unittest.main()