from unittest import TestCase, main

class TestMedianInInterval(TestCase):
    def test_median_in_interval_with_odd_elements(self):
        self.assertTrue(median_in_interval([2, 4, 6, 8, 10], 3, 9))
        self.assertFalse(median_in_interval([2, 4, 6, 8, 10], 1, 5))
        self.assertTrue(median_in_interval([2, 4, 6, 8, 10], 5, 15))
        self.assertFalse(median_in_interval([10, 20, 30, 40, 50], 25, 45))
        self.assertTrue(median_in_interval([10, 20, 30, 40, 50], 5, 55))

    def test_median_in_interval_with_even_elements(self):
        self.assertTrue(median_in_interval([1, 2, 3, 4], 1, 2.5))
        self.assertFalse(median_in_interval([1, 2, 3, 4], 0, 1.5))
        self.assertTrue(median_in_interval([1, 2, 3, 4], 2, 3))
        self.assertFalse(median_in_interval([1, 2, 3, 4], 3.5, 4.5))
        self.assertTrue(median_in_interval([1, 2, 3, 4], -1, 4.5))

if __name__ == '__main__':
    main()