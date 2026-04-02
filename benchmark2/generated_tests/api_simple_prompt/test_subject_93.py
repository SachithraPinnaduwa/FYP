from subject_93 import *

import unittest

class TestCountValidAndPairs(unittest.TestCase):
    def test_case_1(self):
        A = [1, 1, 1, 1, 1]
        expected = 10
        self.assertEqual(count_valid_and_pairs(A), expected)

    def test_case_2(self):
        A = [10]
        expected = 0
        self.assertEqual(count_valid_and_pairs(A), expected)

    def test_case_3(self):
        A = [1, 2, 3, 4, 5]
        expected = 4
        self.assertEqual(count_valid_and_pairs(A), expected)

    def test_case_4(self):
        A = [100, 100, 100, 100, 100]
        expected = 10
        self.assertEqual(count_valid_and_pairs(A), expected)

    def test_case_5(self):
        A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected = 18
        self.assertEqual(count_valid_and_pairs(A), expected)

if __name__ == '__main__':
    unittest.main()