import unittest

def calculate_median(arr):
    n = len(arr)
    middle_index = (n - 1) // 2
    median = arr[middle_index]
    return median

class TestCalculateMedian(unittest.TestCase):

    def test_single_element_array(self):
        self.assertEqual(calculate_median([4]), 4)

    def test_three_elements_array(self):
        self.assertEqual(calculate_median([3, 1, 2]), 2)

    def test_five_elements_array(self):
        self.assertEqual(calculate_median([7, 5, 3, 1, 9]), 5)

    def test_odd_number_of_elements(self):
        self.assertEqual(calculate_median([8, 6, 7, 5, 3, 0, 9]), 7)

    def test_negative_numbers(self):
        self.assertEqual(calculate_median([-3, -1, -2, -4, -5]), -3)

if __name__ == '__main__':
    unittest.main()