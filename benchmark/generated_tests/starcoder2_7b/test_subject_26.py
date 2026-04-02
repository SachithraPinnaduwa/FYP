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

def test_get_similar_rows():
  df = pd.DataFrame({
    'col1': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'col2': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'col3': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'col4': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'col5': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'col6': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'col7': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'col8': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'col9': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'col10': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
  })
  assert get_similar_rows(df, 0.95).all()
  assert get_