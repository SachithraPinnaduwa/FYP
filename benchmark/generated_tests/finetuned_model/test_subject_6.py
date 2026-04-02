import unittest

def find_median(data):
    """
    This function takes a list of numbers as input, sorts the list in ascending order, 
    and returns the median value. It handles both even and odd-length lists.

    Args:
        data (list): A list of numbers.

    Returns:
        float: The median value of the input list.
    """
    # organizing the list in ascending sequence
    data.sort()
    # Finding the middle figure from the sorted sequence
    n = len(data)
    if n % 2 == 0:
        median = (data[n//2 - 1] + data[n//2]) / 2
    else:
        median = data[n//2]
    return median

class TestFindMedian(unittest.TestCase):
    def test_even_length_list(self):
        self.assertEqual(find_median([3, 1, 2, 4, 5]), 3)
        self.assertEqual(find_median([-10, 4, 6, 1000, 10, 20]), 15.0)
        self.assertEqual(find_median([1.5, 2.5, 3.5, 4.5, 5.5, 6.5]), 4.0)

    def test_odd_length_list(self):
        self.assertEqual(find_median([1, 2, 3, 4, 5, 6, 7]), 4)
        self.assertEqual(find_median([-5, 1, 3, 7, 11, 13]), 7)
        self.assertEqual(find_median([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7]), 0.4)

    def test_single_element_list(self):
        self.assertEqual(find_median([42]), 42)

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            find_median([])

    def test_negative_numbers(self):
        self.assertEqual(find_median([-1, -3, -5, -7, -9]), -5)
        self.assertEqual(find_median([-100, -50, 0, 50, 100]), 0)

    def test_repeated_numbers(self):
        self.assertEqual(find_median([1, 1, 1, 1, 1]), 1)
        self.assertEqual(find_median([2, 2, 2, 3, 3, 3]), 2.5)

    def test_mixed_integer_and_float(self):
        self.assertEqual(find_median([1, 2.5, 3, 4.5, 5]), 3)
        self.assertEqual(find_median([-1.5, 0, 1.5, 2.5, 3.5]), 1.5)

if __name__ == '__main__':
    unittest.main()