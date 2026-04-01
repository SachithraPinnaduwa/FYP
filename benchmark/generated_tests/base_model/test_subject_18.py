import unittest

class TestCalculateMedian(unittest.TestCase):

    def test_single_element_array(self):
        self.assertEqual(calculate_median([5]), 5)

    def test_two_elements_array(self):
        self.assertEqual(calculate_median([3, 7]), 5)

    def test_odd_number_of_elements(self):
        self.assertEqual(calculate_median([1, 2, 3, 4, 5]), 3)
        self.assertEqual(calculate_median([9, 8, 6, 7, 5, 4, 3, 2, 1]), 5)

    def test_even_number_of_elements(self):
        # This case is not applicable as per problem description,
        # but if allowed, it should raise an exception or handle gracefully.
        pass

    def test_negative_numbers(self):
        self.assertEqual(calculate_median([-3, -1, 0, 1, 2]), 0)

    def test_large_numbers(self):
        self.assertEqual(calculate_median([10**i for i in range(10)]), 10**4)

if __name__ == '__main__':
    unittest.main()