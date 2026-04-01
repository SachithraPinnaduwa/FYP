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
        self.assertEqual(find_lexicographically_preceding_permutation(3, [1, 3, 2]), [1, 2, 3])

    def test_case_2(self):
        self.assertEqual(find_lexicographically_preceding_permutation(4, [2, 4, 3, 1]), [2, 3, 4, 1])

    def test_case_3(self):
        self.assertEqual(find_lexicographically_preceding_permutation(5, [5, 4, 3, 2, 1]), [5, 4, 3, 1, 2])

    def test_case_4(self):
        self.assertEqual(find_lexicographically_preceding_permutation(6, [1, 2, 3, 4, 6, 5]), [1, 2, 3, 4, 5, 6])

    def test_case_5(self):
        self.assertEqual(find_lexicographically_preceding_permutation(7, [1, 2, 3, 4, 5, 7, 6]), [1, 2, 3, 4, 5, 6, 7])

    def test_case_6(self):
        self.assertEqual(find_lexicographically_preceding_permutation(8, [1, 2, 3, 4, 5, 6, 8, 7]), [1, 2, 3, 4, 5, 6, 7, 8])

if __name__ == '__main__':
    unittest.main()