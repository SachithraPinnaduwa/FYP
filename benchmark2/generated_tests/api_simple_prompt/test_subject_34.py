from subject_34 import *

import unittest

class TestCountSubarraysWithSum(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(count_subarrays_with_sum([1,0,1,0,1], 2), 4)

    def test_case_2(self):
        self.assertEqual(count_subarrays_with_sum([0,0,0,0,0], 0), 15)

    def test_case_3(self):
        self.assertEqual(count_subarrays_with_sum([1,1,1,1,1], 3), 0)

    def test_case_4(self):
        self.assertEqual(count_subarrays_with_sum([1,0,0,1,0,1], 2), 4)

    def test_case_5(self):
        self.assertEqual(count_subarrays_with_sum([0,0,1,0,0,1,0,0,1,0,0], 2), 6)

if __name__ == '__main__':
    unittest.main()