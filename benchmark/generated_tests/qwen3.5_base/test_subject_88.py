import unittest

class TestFindMinDeviationShift(unittest.TestCase):
    def test_case_1(self):
        n = 3
        p = [3, 2, 1]
        res, ires = find_min_deviation_shift(n, p)
        self.assertEqual(res, 0)
        self.assertEqual(ires, 1)
    
    def test_case_2(self):
        n = 4
        p = [4, 3, 2, 1]
        res, ires = find_min_deviation_shift(n, p)
        self.assertEqual(res, 0)
        self.assertEqual(ires, 1)
    
    def test_case_3(self):
        n = 5
        p = [5, 4, 3, 2, 1]
        res, ires = find_min_deviation_shift(n, p)
        self.assertEqual(res, 0)
        self.assertEqual(ires, 1)
    
    def test_case_4(self):
        n = 6
        p = [6, 5, 4, 3, 2, 1]
        res, ires = find_min_deviation_shift(n, p)
        self.assertEqual(res, 0)
        self.assertEqual(ires, 1)
    
    def test_case_5(self):
        n = 7
        p = [7, 6, 5, 4, 3, 2, 1]
        res, ires = find_min_deviation_shift(n, p)
        self.assertEqual(res, 0)
        self.assertEqual(ires, 1)
    
    def test_case_6(self):
        n = 8
        p = [8, 7, 6, 5, 4, 3, 2, 1]
        res, ires = find_min_deviation_shift(n, p)
        self.assertEqual(res, 0)
        self.assertEqual(ires, 1)
    
    def test_case_7(self):
        n = 9
        p = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        res, ires = find_min_deviation_shift(n, p)
        self.assertEqual(res, 0)
        self.assertEqual(ires, 1)
    
    def test_case_8(self):
        n = 10
        p = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        res, ires = find_min_deviation_shift(n, p)
        self.assertEqual(res, 0)
        self.assertEqual(ires, 1)
    
    def test_case_9(self):
        n = 11
        p = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        res, ires = find_min_deviation_shift(n, p)
        self.assertEqual(res, 0)
        self.assertEqual(ires, 1)
    
    def test_case_10(self):
        n = 12
        p = [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        res, ires = find_min_deviation_shift(n, p)
        self.assertEqual(res, 0)
        self.assertEqual(ires, 1)
    
    def test_case_11(self):
        n = 13
        p = [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        res, ires = find_min_deviation_shift(n, p)
        self.assertEqual(res, 0)
        self.assertEqual(ires, 1)
    
    def test_case_12(self):
        n = 14
        p = [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        res, ires = find_min_deviation_shift(n, p)
        self.assertEqual(res, 0)
        self.assertEqual(ires, 1)
    
    def test_case_13(self):
        n = 15
        p = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        res, ires = find_min_deviation_shift(n, p)
        self.assertEqual(res, 0)
        self.assertEqual(ires, 1)
    
    def test_case_14(self):
        n = 16
        p = [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        res, ires = find_min_deviation_shift(n, p)
        self.assertEqual(res, 0)
        self.assertEqual(ires, 1)
    
    def test_case_15(self):
        n = 17
        p = [17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        res, ires = find_min_deviation_shift(n, p)
        self.assertEqual(res, 0)
        self.assertEqual(ires, 1)
    
    def test_case_16(self):
        n = 18
        p = [18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        res, ires = find_min_deviation_shift(n, p)
        self.assertEqual(res, 0)
        self.assertEqual(ires, 1)
    
    def test_case_17(self):
        n = 19
        p = [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3