from subject_33 import *

import unittest

def max_marks_with_forgetfulness(chapters, total_time):
    """
    Calculate the maximum marks Chef can score in the exam given the constraints.

    Parameters:
    - chapters (list of tuples): Each tuple contains (marks, time) for a chapter.
    - total_time (int): Total time left before the exam.

    Returns:
    - int: The maximum marks Chef can score.
    """
    n = len(chapters)
    dp = [[0, -float('inf')] for i in range(total_time + 1)]
    
    for i in range(n):
        (m, t) = chapters[i]
        for j in range(total_time, t - 1, -1):
            dp[j][0] = max(dp[j - t][0] + m, dp[j][0])
            dp[j][1] = max(dp[j][1], dp[j - t][0], dp[j - t][1] + m)
    
    return dp[total_time][1]

class TestMaxMarksWithForgetfulness(unittest.TestCase):
    def test_normal_case_1(self):
        self.assertEqual(max_marks_with_forgetfulness([(1, 1), (2, 1)], 2), 2)

    def test_normal_case_2(self):
        self.assertEqual(max_marks_with_forgetfulness([(1, 1), (2, 2), (3, 3)], 3), 2)

    def test_normal_case_3(self):
        self.assertEqual(max_marks_with_forgetfulness([(5, 1), (4, 2), (3, 3), (2, 4), (1, 5)], 6), 9)

    def test_edge_case_1(self):
        self.assertEqual(max_marks_with_forgetfulness([(1, 2)], 1), 0)

    def test_edge_case_2(self):
        self.assertEqual(max_marks_with_forgetfulness([(1, 1)], 0), 0)

    def test_error_handling_1(self):
        self.assertEqual(max_marks_with_forgetfulness([], 1), 0)

if __name__ == '__main__':
    unittest.main()