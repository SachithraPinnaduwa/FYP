import unittest

class TestSmallestPositiveNoCompare(unittest.TestCase):
    def test_smallest_positive_no_compare(self):
        self.assertEqual(smallest_positive_no_compare([1, 2, 3, 4, 5]), 1)
        self.assertEqual(smallest_positive_no_compare([1, 2, 3, 4, 5, 0]), 1)
        self.assertEqual(smallest_positive_no_compare([1, 2, 3, 4, 5, -1]), 1)
        self.assertEqual(smallest_positive_no_compare([1, 2, 3, 4, 5, -1, -2]), 1)
        self.assertEqual(smallest_positive_no_compare([1, 2, 3, 4, 5, -1, -2, -3]), 1)
        self.assertEqual(smallest_positive_no_compare([1, 2, 3, 4, 5, -1, -2, -3, -4]), 1)
        self.assertEqual(smallest_positive_no_compare([1, 2, 3, 4, 5, -1, -2, -3, -4, -5]), 1)
        self.assertEqual(smallest_positive_no_compare([1, 2, 3, 4, 5, -1, -2, -3, -4, -5, -6]), 1)
        self.assertEqual(smallest_positive_no_compare([1, 2, 3, 4, 5, -1, -2, -3, -4, -5, -6, -7]), 1)
        self.assertEqual(smallest_positive_no_compare([1, 2, 3, 4, 5, -1, -2, -3, -4, -5, -6, -7, -8]), 1)
        self.assertEqual(smallest_positive_no_compare([1, 2, 3, 4, 5, -1, -2, -3, -4, -5, -6, -7, -8, -9]), 1)
        self.assertEqual(smallest_positive_no_compare([1, 2, 3, 4, 5, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]), 1)
        self.assertEqual(smallest_positive_no_compare([1, 2, 3, 4, 5, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11]), 1)
        self.assertEqual(smallest_positive_no_compare([1, 2, 3, 4, 5, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12]), 1)
        self.assertEqual(smallest_positive_no_compare([1, 2, 3, 4, 5, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13]), 1)
        self.assertEqual(smallest_positive_no_compare([1, 2, 3, 4, 5, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14]), 1)
        self.assertEqual(smallest_positive_no_compare([1, 2, 3, 4, 5, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15]), 1)
        self.assertEqual(smallest_positive_no_compare([1, 2, 3, 4, 5, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16]), 1)
        self.assertEqual(smallest_positive_no_compare([1, 2, 3, 4, 5, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17]), 1)
        self.assertEqual(smallest_positive_no_compare([1, 2, 3, 4, 5, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18]), 1)
        self.assertEqual(smallest_positive_no_compare([1, 2, 3, 4, 5, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19]), 1)
        self.assertEqual(smallest_positive_no_compare([1, 2, 3, 4, 5, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20]), 1)
        self.assertEqual(smallest_positive_no_compare([1, 2, 3, 4, 5, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20, -21]), 1)
        self.assertEqual(smallest_positive_no_compare([1, 2, 3, 4, 5, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20, -21, -22]), 1)
        self.assertEqual(smallest_positive_no_compare([1, 2