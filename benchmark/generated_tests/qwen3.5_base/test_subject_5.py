import unittest

class TestFindLexicographicallyPrecedingPermutation(unittest.TestCase):
    def test_case_1(self):
        n = 3
        permutation = [1, 2, 3]
        result = find_lexicographically_preceding_permutation(n, permutation)
        self.assertEqual(result, [1, 2, 3])
    
    def test_case_2(self):
        n = 3
        permutation = [3, 2, 1]
        result = find_lexicographically_preceding_permutation(n, permutation)
        self.assertEqual(result, [1, 2, 3])
    
    def test_case_3(self):
        n = 4
        permutation = [1, 2, 3, 4]
        result = find_lexicographically_preceding_permutation(n, permutation)
        self.assertEqual(result, [1, 2, 3, 4])
    
    def test_case_4(self):
        n = 4
        permutation = [4, 3, 2, 1]
        result = find_lexicographically_preceding_permutation(n, permutation)
        self.assertEqual(result, [1, 2, 3, 4])
    
    def test_case_5(self):
        n = 5
        permutation = [1, 2, 3, 4, 5]
        result = find_lexicographically_preceding_permutation(n, permutation)
        self.assertEqual(result, [1, 2, 3, 4, 5])
    
    def test_case_6(self):
        n = 5
        permutation = [5, 4, 3, 2, 1]
        result = find_lexicographically_preceding_permutation(n, permutation)
        self.assertEqual(result, [1, 2, 3, 4, 5])
    
    def test_case_7(self):
        n = 6
        permutation = [1, 2, 3, 4, 5, 6]
        result = find_lexicographically_preceding_permutation(n, permutation)
        self.assertEqual(result, [1, 2, 3, 4, 5, 6])
    
    def test_case_8(self):
        n = 6
        permutation = [6, 5, 4, 3, 2, 1]
        result = find_lexicographically_preceding_permutation(n, permutation)
        self.assertEqual(result, [1, 2, 3, 4, 5, 6])
    
    def test_case_9(self):
        n = 7
        permutation = [1, 2, 3, 4, 5, 6, 7]
        result = find_lexicographically_preceding_permutation(n, permutation)
        self.assertEqual(result, [1, 2, 3, 4, 5, 6, 7])
    
    def test_case_10(self):
        n = 7
        permutation = [7, 6, 5, 4, 3, 2, 1]
        result = find_lexicographically_preceding_permutation(n, permutation)
        self.assertEqual(result, [1, 2, 3, 4, 5, 6, 7])
    
    def test_case_11(self):
        n = 8
        permutation = [1, 2, 3, 4, 5, 6, 7, 8]
        result = find_lexicographically_preceding_permutation(n, permutation)
        self.assertEqual(result, [1, 2, 3, 4, 5, 6, 7, 8])
    
    def test_case_12(self):
        n = 8
        permutation = [8, 7, 6, 5, 4, 3, 2, 1]
        result = find_lexicographically_preceding_permutation(n, permutation)
        self.assertEqual(result, [1, 2, 3, 4, 5, 6, 7, 8])
    
    def test_case_13(self):
        n = 9
        permutation = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        result = find_lexicographically_preceding_permutation(n, permutation)
        self.assertEqual(result, [1, 2, 3, 4, 5, 6, 7, 8, 9])
    
    def test_case_14(self):
        n = 9
        permutation = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        result = find_lexicographically_preceding_permutation(n, permutation)
        self.assertEqual(result, [1, 2, 3, 4, 5, 6, 7, 8, 9])
    
    def test_case_15(self):
        n = 10
        permutation = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        result = find_lexicographically_preceding_permutation(n, permutation)
        self.assertEqual(result, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    
    def test_case_16(self):
        n = 10
        permutation = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        result = find_lexicographically_preceding_permutation(n, permutation)
        self.assertEqual(result, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    
    def test_case_17(self):
        n = 11
        permutation = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        result = find_lexicographically_preceding_permutation(n, permutation)
        self.assertEqual(result, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
    
    def test_case_18(self):
        n = 11
        permutation = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        result = find_lexicographically_preceding_permutation(n, permutation)
        self.assertEqual(result, [1,