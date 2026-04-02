import unittest

class TestFindMedian(unittest.TestCase):
    def test_find_median_odd_length(self):
        self.assertEqual(find_median([1, 2, 3]), 2)
        self.assertEqual(find_median([1, 2, 3, 4, 5]), 3)
        self.assertEqual(find_median([1, 2, 3, 4, 5, 6, 7]), 4)
        self.assertEqual(find_median([1, 2, 3, 4, 5, 6, 7, 8, 9]), 5)
        self.assertEqual(find_median([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 5)
        self.assertEqual(find_median([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), 6)
        self.assertEqual(find_median([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]), 6)
        self.assertEqual(find_median([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]), 7)
        self.assertEqual(find_median([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]), 7)
        self.assertEqual(find_median([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), 8)
        self.assertEqual(find_median([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]), 8)
        self.assertEqual(find_median([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]), 9)
        self.assertEqual(find_median([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]), 9)
        self.assertEqual(find_median([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]), 10)
        self.assertEqual(find_median([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]), 10)
        self.assertEqual(find_median([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]), 11)
        self.assertEqual(find_median([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]), 11)
        self.assertEqual(find_median([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]), 12)
        self.assertEqual(find_median([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]), 12)
        self.assertEqual(find_median([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]), 13)
        self.assertEqual(find_median([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), 13)
        self.assertEqual(find_median([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]), 14)
        self.assertEqual(find_median([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,