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
    def test_get_similar_rows(self):
        # Test case 1: Basic test with a simple DataFrame
        data = {
            'A': [1, 2, 3, 4],
            'B': [5, 6, 7, 8],
            'C': [9, 10, 11, 12]
        }
        df = pd.DataFrame(data)
        threshold = 0.95
        expected_mask = np.array([True, False, False, False])
        self.assertTrue(np.array_equal(get_similar_rows(df, threshold), expected_mask))

        # Test case 2: Test with a DataFrame where all rows are similar
        data = {
            'A': [1, 1, 1, 1],
            'B': [2, 2, 2, 2],
            'C': [3, 3, 3, 3]
        }
        df = pd.DataFrame(data)
        threshold = 0.95
        expected_mask = np.array([True, True, True, True])
        self.assertTrue(np.array_equal(get_similar_rows(df, threshold), expected_mask))

        # Test case 3: Test with a DataFrame where no rows are similar
        data = {
            'A': [1, 2, 3, 4],
            'B': [5, 6, 7, 8],
            'C': [9, 10, 11, 12]
        }
        df = pd.DataFrame(data)
        threshold = 1.0
        expected_mask = np.array([False, False, False, False])
        self.assertTrue(np.array_equal(get_similar_rows(df, threshold), expected_mask))

        # Test case 4: Test with a DataFrame where some rows are similar
        data = {
            'A': [1, 2, 3, 4],
            'B': [2, 2, 2, 2],
            'C': [3, 3, 3, 3]
        }
        df = pd.DataFrame(data)
        threshold = 0.95
        expected_mask = np.array([True, True, True, False])
        self.assertTrue(np.array_equal(get_similar_rows(df, threshold), expected_mask))

        # Test case 5: Test with a DataFrame where rows have different data types
        data = {
            'A': [1, 2, 3, 4],
            'B': [5, 6, 7, 8],
            'C': ['a', 'b', 'c', 'd']
        }
        df = pd.DataFrame(data)
        threshold = 0.95
        expected_mask = np.array([False, False, False, False])
        self.assertTrue(np.array_equal(get_similar_rows(df, threshold), expected_mask))

if __name__ == '__main__':
    unittest.main()