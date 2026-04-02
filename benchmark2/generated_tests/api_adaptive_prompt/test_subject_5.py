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
    def test_normal_case_1(self):
        n = 3
        permutation = [1, 3, 2]
        expected = [1, 2, 3]
        self.assertEqual(find_lexicographically_preceding_permutation(n, permutation), expected)

    def test_normal_case_2(self):
        n = 3
        permutation = [1, 2, 3]
        expected = [1, 2, 3]
        self.assertEqual(find_lexicographically_preceding_permutation(n, permutation), expected)

    def test_normal_case_3(self):
        n = 3
        permutation = [3, 2, 1]
        expected = [3, 2, 1]
        self.assertEqual(find_lexicographically_preceding_permutation(n, permutation), expected)

    def test_edge_case_1(self):
        n = 1
        permutation = [1]
        expected = [1]
        self.assertEqual(find_lexicographically_preceding_permutation(n, permutation), expected)

    def test_edge_case_2(self):
        n = 1000000
        permutation = [i for i in range(1, 1000001)]
        expected = [i for i in range(1, 1000001)]
        self.assertEqual(find_lexicographically_preceding_permutation(n, permutation), expected)

    def test_error_handling_1(self):
        n = 0
        permutation = []
        expected = []
        self.assertEqual(find_lexicographically_preceding_permutation(n, permutation), expected)

    def test_error_handling_2(self):
        n = 3
        permutation = [1, '3', 2]
        expected = [1, '3', 2]
        self.assertEqual(find_lexicographically_preceding_permutation(n, permutation), expected)

    def test_error_handling_3(self):
        n = 3
        permutation = [1, -3, 2]
        expected = [1, -3, 2]
        self.assertEqual(find_lexicographically_preceding_permutation(n, permutation), expected)

if __name__ == '__main__':
    unittest.main()