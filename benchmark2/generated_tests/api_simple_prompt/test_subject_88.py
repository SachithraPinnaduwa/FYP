from subject_88 import *

import unittest

def find_min_deviation_shift(n, p):
    res = 0
    ires = 0
    neg = 0
    when = [0] * n
    
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
    def test_case_1(self):
        n = 3
        p = [1, 2, 3]
        expected = (0, 0)
        self.assertEqual(find_min_deviation_shift(n, p), expected)
    
    def test_case_2(self):
        n = 3
        p = [2, 3, 1]
        expected = (0, 1)
        self.assertEqual(find_min_deviation_shift(n, p), expected)
    
    def test_case_3(self):
        n = 3
        p = [3, 2, 1]
        expected = (2, 1)
        self.assertEqual(find_min_deviation_shift(n, p), expected)
    
    def test_case_4(self):
        n = 4
        p = [4, 3, 2, 1]
        expected = (0, 0)
        self.assertEqual(find_min_deviation_shift(n, p), expected)
    
    def test_case_5(self):
        n = 5
        p = [5, 1, 2, 3, 4]
        expected = (0, 0)
        self.assertEqual(find_min_deviation_shift(n, p), expected)
    
    def test_case_6(self):
        n = 5
        p = [1, 5, 2, 3, 4]
        expected = (2, 1)
        self.assertEqual(find_min_deviation_shift(n, p), expected)
    
    def test_case_7(self):
        n = 5
        p = [1, 2, 5, 3, 4]
        expected = (4, 1)
        self.assertEqual(find_min_deviation_shift(n, p), expected)
    
    def test_case_8(self):
        n = 5
        p = [1, 2, 3, 5, 4]
        expected = (6, 1)
        self.assertEqual(find_min_deviation_shift(n, p), expected)
    
    def test_case_9(self):
        n = 5
        p = [1, 2, 3, 4, 5]
        expected = (0, 0)
        self.assertEqual(find_min_deviation_shift(n, p), expected)
    
    def test_case_10(self):
        n = 10
        p = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        expected = (0, 0)
        self.assertEqual(find_min_deviation_shift(n, p), expected)

if __name__ == '__main__':
    unittest.main()