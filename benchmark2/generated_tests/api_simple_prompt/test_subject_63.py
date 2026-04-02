from subject_63 import *

import unittest

def entrance(n, cache = {}):
  if n in cache:
    return cache[n]
  elif n <= 1:
    value = n
  else:
    value = entrance(n-1, cache) + entrance(n-2, cache)
  cache[n] = value
  return value

class TestEntranceFunction(unittest.TestCase):
    def test_base_cases(self):
        self.assertEqual(entrance(0), 0)
        self.assertEqual(entrance(1), 1)

    def test_small_values(self):
        self.assertEqual(entrance(2), 1)
        self.assertEqual(entrance(3), 2)
        self.assertEqual(entrance(4), 3)

    def test_large_values(self):
        self.assertEqual(entrance(10), 55)
        self.assertEqual(entrance(20), 6765)
        self.assertEqual(entrance(30), 832040)

    def test_with_cache(self):
        self.assertEqual(entrance(5, {3: 2, 4: 3}), 5)
        self.assertEqual(entrance(7, {5: 5, 6: 8}), 13)

if __name__ == '__main__':
    unittest.main()