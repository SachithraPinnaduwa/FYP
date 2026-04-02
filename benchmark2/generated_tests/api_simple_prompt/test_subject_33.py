from subject_33 import *

import unittest

def max_marks_with_forgetfulness(chapters, total_time):
    n = len(chapters)
    dp = [[0, -float('inf')] for i in range(total_time + 1)]
    
    for i in range(n):
        (m, t) = chapters[i]
        for j in range(total_time, t - 1, -1):
            dp[j][0] = max(dp[j - t][0] + m, dp[j][0])
            dp[j][1] = max(dp[j][1], dp[j - t][0], dp[j - t][1] + m)
    
    return dp[total_time][1]

class TestMaxMarksWithForgetfulness(unittest.TestCase):
    def test_case_1(self):
        chapters = [(1, 1), (2, 1)]
        total_time = 2
        expected = 2
        self.assertEqual(max_marks_with_forgetfulness(chapters, total_time), expected)

    def test_case_2(self):
        chapters = [(1, 1), (2, 2), (3, 3)]
        total_time = 3
        expected = 2
        self.assertEqual(max_marks_with_forgetfulness(chapters, total_time), expected)

    def test_case_3(self):
        chapters = [(5, 1), (4, 2), (3, 3), (2, 4), (1, 5)]
        total_time = 6
        expected = 9
        self.assertEqual(max_marks_with_forgetfulness(chapters, total_time), expected)

if __name__ == '__main__':
    unittest.main()