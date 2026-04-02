import unittest

class Test(unittest.TestCase):
    def test_find_lexicographically_preceding_permutation(self):
        self.assertEqual(find_lexicographically_preceding_permutation(3, [1, 3, 2]), [1, 2, 3])
        self.assertEqual(find_lexicographically_preceding_permutation(3, [1, 2, 3]), [1, 2, 3])
        self.assertEqual(find_lexicographically_preceding_permutation(3, [3, 2, 1]), [3, 1, 2])
        self.assertEqual(find_lexicographically_preceding_permutation(3, [2, 1, 3]), [2, 3, 1])
        self.assertEqual(find_lexicographically_preceding_permutation(3, [2, 3, 1]), [2, 1, 3])
        self.assertEqual(find_lexicographically_preceding_permutation(3, [3, 1, 2]), [3, 2, 1])
        self.assertEqual(find_lexicographically_preceding_permutation(3, [1, 1, 1]), [1, 1, 1])
        self.assertEqual(find_lexicographically_preceding_permutation(3, [1, 2, 2]), [1, 2, 2])
        self.assertEqual(find_lexicographically_preceding_permutation(3, [2, 2, 1]), [2, 2, 1])
        self.assertEqual(find_lexicographically_preceding_permutation(3, [2, 1, 2]), [2, 1, 2])
        self.assertEqual(find_lexicographically_preceding_permutation(3, [2, 2, 2]), [2, 2, 2])
        self.assertEqual(find_lexicographically_preceding_permutation(3, [2, 3, 3]), [2, 3, 3])
        self.assertEqual(find_lexicographically_preceding_permutation(3, [3, 3