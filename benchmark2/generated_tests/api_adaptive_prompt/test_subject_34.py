from subject_34 import *

import unittest

def count_subarrays_with_sum(A, S):
    ans = 0
    if S == 0:
        c = 0
        for i in range(len(A)):
            if A[i] == 0:
                c += 1
            else:
                c = 0
            ans += c
        return ans
    
    l = [-1]
    for i in range(len(A)):
        if A[i] == 1:
            l.append(i)
    l.append(len(A))
    
    ans = 0
    for i in range(1, len(l) - S):
        ans += (l[i] - l[i - 1]) * (l[i + S] - l[i + S - 1])
    
    return ans

class TestCountSubarraysWithSum(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual(count_subarrays_with_sum([1, 0, 1, 0, 1], 2), 4)

    def test_edge_case_all_zeros(self):
        self.assertEqual(count_subarrays_with_sum([0, 0, 0], 0), 6)

    def test_edge_case_all_ones(self):
        self.assertEqual(count_subarrays_with_sum([1, 1, 1], 3), 3)

    def test_edge_case_empty_array(self):
        self.assertEqual(count_subarrays_with_sum([], 0), 0)

    def test_edge_case_all_zeros_sum_equal_length(self):
        self.assertEqual(count_subarrays_with_sum([0, 0, 0], 3), 0)

    def test_error_handling_negative_sum(self):
        with self.assertRaises(ValueError):
            count_subarrays_with_sum([1, 0, 1, 0, 1], -1)

if __name__ == '__main__':
    unittest.main()