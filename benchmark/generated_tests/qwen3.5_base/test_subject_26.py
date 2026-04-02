import unittest

class TestGetSimilarRows(unittest.TestCase):
  def test_get_similar_rows(self):
    df = pd.DataFrame({
      'A': [1, 2, 3, 4, 5],
      'B': [1, 2, 3, 4, 5],
      'C': [1, 2, 3, 4, 5],
    })
    mask = get_similar_rows(df, 0.5)
    self.assertTrue(mask[0])
    self.assertTrue(mask[1])
    self.assertTrue(mask[2])
    self.assertTrue(mask[3])
    self.assertTrue(mask[4])

if __name__ == '__main__':
  unittest.main()
