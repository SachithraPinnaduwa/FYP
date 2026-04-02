from subject_1 import *

import unittest

def median_in_interval(numbers, lower_limit, upper_limit):
    numbers.sort()
    if len(numbers) % 2 == 0:  # Even number of elements
        median = (numbers[len(numbers)//2 - 1] + numbers[len(numbers)//2]) / 2
    else:  # Odd number of elements
        median = numbers[len(numbers)//2]
    return lower_limit <= median <= upper_limit

class TestMedianInInterval(unittest.TestCase):
    def test_median_in_interval(self):
        self.assertTrue(median_in_interval([1, 3, 5, 7], 2, 6))
        self.assertFalse(median_in_interval([1, 3, 5, 7], 8, 10))
        self.assertTrue(median_in_interval([10, 20, 30, 40, 50], 25, 45))
        self.assertFalse(median_in_interval([10, 20, 30, 40, 50], 1, 9))
        self.assertTrue(median_in_interval([100], 100, 100))
        self.assertFalse(median_in_interval([100], 99, 101))
        self.assertTrue(median_in_interval([1, 2, 3, 4, 5, 6], 3, 4))
        self.assertFalse(median_in_interval([1, 2, 3, 4, 5, 6], 5, 7))

if __name__ == '__main__':
    unittest.main()