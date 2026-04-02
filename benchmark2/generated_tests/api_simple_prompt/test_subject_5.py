from subject_5 import *

import unittest

def find_lexicographically_preceding_permutation(n, permutation):
    b = []
    flag = 0
    
    for x in range(n-1, 0, -1):
        b = permutation[:x-1]
        if permutation[x] < permutation[x-1]:
            for y in range(n-1, x-1, -1):
                if permutation[x-1] > permutation[y]:
                    b.append(permutation[y])
                    flag = 1
                    c = permutation[x-1:]
                    del(c[y-x+1])
                    c.sort()
                    c.reverse()
                    b = b + c
                if flag == 1:
                    break
        if flag == 1:
            break
    
    if flag == 0:
        return permutation
    else:
        return b

class TestFindLexicographicallyPrecedingPermutation(unittest.TestCase):
    def test_case_1(self):
        n = 3
        permutation = [1, 3, 2]
        expected_output = [1, 2, 3]
        self.assertEqual(find_lexicographically_preceding_permutation(n, permutation), expected_output)
    
    def test_case_2(self):
        n = 4
        permutation = [1, 2, 4, 3]
        expected_output = [1, 2, 3, 4]
        self.assertEqual(find_lexicographically_preceding_permutation(n, permutation), expected_output)
    
    def test_case_3(self):
        n = 5
        permutation = [2, 1, 5, 4, 3]
        expected_output = [2, 1, 5, 3, 4]
        self.assertEqual(find_lexicographically_preceding_permutation(n, permutation), expected_output)
    
    def test_case_4(self):
        n = 6
        permutation = [1, 2, 3, 6, 5, 4]
        expected_output = [1, 2, 3, 5, 6, 4]
        self.assertEqual(find_lexicographically_preceding_permutation(n, permutation), expected_output)
    
    def test_case_5(self):
        n = 7
        permutation = [1, 2, 3, 4, 7, 6, 5]
        expected_output = [1, 2, 3, 4, 7, 5, 6]
        self.assertEqual(find_lexicographically_preceding_permutation(n, permutation), expected_output)
    
    def test_case_6(self):
        n = 8
        permutation = [1, 2, 3, 4, 5, 8, 7, 6]
        expected_output = [1, 2, 3, 4, 5, 8, 6, 7]
        self.assertEqual(find_lexicographically_preceding_permutation(n, permutation), expected_output)
    
    def test_case_7(self):
        n = 9
        permutation = [1, 2, 3, 4, 5, 6, 9, 8, 7]
        expected_output = [1, 2, 3, 4, 5, 6, 9, 7, 8]
        self.assertEqual(find_lexicographically_preceding_permutation(n, permutation), expected_output)
    
    def test_case_8(self):
        n = 10
        permutation = [1, 2, 3, 4, 5, 6, 7, 10, 9, 8]
        expected_output = [1, 2, 3, 4, 5, 6, 7, 10, 8, 9]
        self.assertEqual(find_lexicographically_preceding_permutation(n, permutation), expected_output)
    
    def test_case_9(self):
        n = 11
        permutation = [1, 2, 3, 4, 5, 6, 7, 8, 11, 10, 9]
        expected_output = [1, 2, 3, 4, 5, 6, 7, 8, 11, 9, 10]
        self.assertEqual(find_lexicographically_preceding_permutation(n, permutation), expected_output)
    
    def test_case_10(self):
        n = 12
        permutation = [1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 11, 10]
        expected_output = [1, 2, 3, 4, 5, 6, 7, 