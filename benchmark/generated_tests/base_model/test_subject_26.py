import unittest
import pandas as pd
import numpy as np
from your_module import get_similar_rows

class TestGetSimilarRows(unittest.TestCase):

    def setUp(self):
        self.df1 = pd.DataFrame({
            'A': [1, 2, 3, 4],
            'B': [5, 6, 7, 8],
            'C': [9, 10, 11, 12]
        })
        self.threshold1 = 0.95

        self.df2 = pd.DataFrame({
            'A': [1, 2, 2, 4],
            'B': [5, 6, 6, 8],
            'C': [9, 10, 10, 12]
        })
        self.threshold2 = 0.95

        self.df3 = pd.DataFrame({
            'A': [1, 2, 3, 4],
            'B': [5, 6, 7, 8],
            'C': [9, 10, 11, 12]
        })
        self.threshold3 = 0.8

    def test_get_similar_rows_identical_columns(self):
        result = get_similar_rows(self.df1, self.threshold1)
        expected = np.array([True, True, True, True])
        self.assertTrue(np.array_equal(result, expected))

    def test_get_similar_rows_partial_match(self):
        result = get_similar_rows(self.df2, self.threshold2)
        expected = np.array([True, False, True, False])
        self.assertTrue(np.array_equal(result, expected))

    def test_get_similar_rows_low_threshold(self):
        result = get_similar_rows(self.df3, self.threshold3)
        expected = np.array([False, False, False, False])
        self.assertTrue(np.array_equal(result, expected))

if __name__ == '__main__':
    unittest.main()