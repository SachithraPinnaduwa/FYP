from subject_47 import *

import unittest

def median(l: list, cmp_func: callable):
    l_len = len(l)
    if l_len == 0: 
        return None
    counts = [(sum(1 for j in l if cmp_func(i, j) > 0),
               sum(1 for j in l if cmp_func(i, j) < 0)) for i in l]
    try:
        if l_len % 2 == 1:
            return next(l[i] for i in range(l_len) if max(counts[i]) == (l_len - 1 )// 2)
        else:
            lo = next(l[i] for i in range(l_len) if counts[i][1] == l_len//2 - 1 and counts[i][0] <= l_len//2)
            hi = next(l[i] for i in range(l_len) if counts[i][1] <= l_len//2 and counts[i][0] == l_len//2 - 1)
            return (lo+hi)/2
    except StopIteration:
        return None

class TestMedian(unittest.TestCase):
    def test_median_odd_list(self):
        self.assertEqual(median([1, 3, 3, 6, 7, 8, 9], lambda x, y: x - y), 6)
    
    def test_median_even_list(self):
        self.assertEqual(median([1, 2, 3, 4, 5, 6], lambda x, y: x - y), 3.5)
    
    def test_median_empty_list(self):
        self.assertIsNone(median([], lambda x, y: x - y))
    
    def test_median_mismatched_types(self):
        self.assertIsNone(median([1, 'a', 3], lambda x, y: x - y))
    
    def test_median_duplicate_elements(self):
        self.assertEqual(median([1, 1, 1, 1, 1], lambda x, y: x - y), 1)
    
    def test_median_custom_comparison(self):
        self.assertEqual(median(['apple', 'banana', 'cherry'], lambda x, y: len(x) - len(y)), 'apple')

if __name__ == '__main__':
    unittest.main()