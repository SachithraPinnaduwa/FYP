from subject_26 import *

import unittest
import pandas as pd
import numpy as np
import itertools

def get_similar_rows(df, threshold):
  mask = np.zeros(len(df), dtype=bool)
  for i,j in itertools.combinations(range(len(df)), 2):
    similarity = sum(df.iloc[i] == df.iloc[j]) / len(df.columns)
    if similarity >= threshold:
      mask[i] = True
      mask[j] = True
  return mask

class TestGetSimilarRows(unittest.TestCase):
    def test_normal_case_multiple_rows_high_threshold(self):
        df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
        threshold = 0.95
        expected = np.array([True, True, False])
        self.assertTrue(np.array_equal(get_similar_rows(df, threshold), expected))

    def test_normal_case_mixed_matching_columns(self):
        df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
        threshold = 0.9
        expected = np.array([True, True, False])
        self.assertTrue(np.array_equal(get_similar_rows(df, threshold), expected))

    def test_normal_case_high_matching_columns(self):
        df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
        threshold = 0.98
        expected = np.array([True, True, False])
        self.assertTrue(np.array_equal(get_similar_rows(df, threshold), expected))

    def test_normal_case_low_matching_columns(self):
        df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
        threshold = 0.85
        expected = np.array([False, False, False])
        self.assertTrue(np.array_equal(get_similar_rows(df, threshold), expected))

    def test_edge_case_empty_dataframe(self):
        df = pd.DataFrame()
        threshold = 0.95
        expected = np.array([])
        self.assertTrue(np.array_equal(get_similar_rows(df, threshold), expected))

    def test_edge_case_single_row_dataframe(self):
        df = pd.DataFrame({'A': [1], 'B': [2], 'C': [3]})
        threshold = 0.95
        expected = np.array([])
        self.assertTrue(np.array_equal(get_similar_rows(df, threshold), expected))

    def test_error_handling_non_dataframe_input(self):
        df = 'not a DataFrame'
        threshold = 0.95
        with self.assertRaises(TypeError):
            get_similar_rows(df, threshold)

    def test_error_handling_non_numeric_threshold(self):
        df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
        threshold = 'not a number'
        with self.assertRaises(ValueError):
            get_similar_rows(df, threshold)

    def test_error_handling_threshold_outside_valid_range(self):
        df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
        threshold = 1.1
        with self.assertRaises(ValueError):
            get_similar_rows(df, threshold)

if __name__ == '__main__':
    unittest.main()