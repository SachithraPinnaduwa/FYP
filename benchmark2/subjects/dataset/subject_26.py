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