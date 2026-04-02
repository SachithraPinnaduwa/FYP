import unittest

class Test(unittest.TestCase):
    def test_count_subarrays_with_sum(self):
        self.assertEqual(count_subarrays_with_sum([1,0,1,0,1], 2), 4)
        self.assertEqual(count_subarrays_with_sum([1,0,1,0,1], 0), 10)
        self.assertEqual(count_subarrays_with_sum([1,0,1,0,1], 1), 10)
        self.assertEqual(count_subarrays_with_sum([1,0,1,0,1], 3), 0)
        self.assertEqual(count_subarrays_with_sum([1,0,1,0,1], 4), 0)
        self.assertEqual(count_subarrays_with_sum([1,0,1,0,1], 5), 0)
        self.assertEqual(count_subarrays_with_sum([1,0,1,0,1], 6), 0)
        self.assertEqual(count_subarrays_with_sum([1,0,1,0,1], 7), 0)
        self.assertEqual(count_subarrays_with_sum([1,0,1,0,1], 8), 0)
        self.assertEqual(count_subarrays_with_sum([1,0,1,0,1], 9), 0)
        self.assertEqual(count_subarrays_with_sum([1,0,1,0,1], 10), 0)
        self.assertEqual(count_subarrays_with_sum([1,0,1,0,1], 11), 0)
        self.assertEqual(count_subarrays_with_sum([1,0,1,0,1], 12), 0)
        self.assertEqual(count_subarrays_with_sum([1,0,1,0,1], 13), 0)
        self.assertEqual(count_subarrays_with_sum([1,0,1,0,1], 14), 0)
        self.assertEqual(count_subarrays_with_sum([1,0,1,0,1], 15),