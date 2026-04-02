import unittest

def median_in_interval(numbers, lower_limit, upper_limit):
    numbers.sort()
    if len(numbers) % 2 == 0:  # Even number of elements
        median = (numbers[len(numbers)//2 - 1] + numbers[len(numbers)//2]) / 2
    else:  # Odd number of elements
        median = numbers[len(numbers)//2]
    return lower_limit <= median <= upper_limit

class TestMedianInInterval(unittest.TestCase):

    def test_median_even(self):
        self.assertTrue(median_in_interval([3, 1, 4, 1, 5, 9], 2, 6))
    
    def test_median_odd(self):
        self.assertFalse(median_in_interval([3, 1, 4, 1, 5], 3, 7))
    
    def test_empty_list(self):
        self.assertFalse(median_in_interval([], 0, 10))
    
    def test_single_element(self):
        self.assertTrue(median_in_interval([5], 5, 5))
    
    def test_all_outside_range(self):
        self.assertFalse(median_in_interval([1, 2, 3, 4], 5, 8))
    
    def test_all_inside_range(self):
        self.assertTrue(median_in_interval([1, 2, 3, 4], 0, 5))

if __name__ == '__main__':
    unittest.main()