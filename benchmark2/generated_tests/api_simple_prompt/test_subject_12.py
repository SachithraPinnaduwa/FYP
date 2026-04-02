from subject_12 import *

import unittest

def entance(n):
    if n <= 1:
       return n
    else:
       return (entance(n-1) + entance(n-2))

class TestEntanceFunction(unittest.TestCase):
    def test_base_cases(self):
        self.assertEqual(entance(0), 0)
        self.assertEqual(entance(1), 1)

    def test_small_numbers(self):
        self.assertEqual(entance(2), 1)
        self.assertEqual(entance(3), 2)
        self.assertEqual(entance(4), 3)

    def test_large_numbers(self):
        self.assertEqual(entance(10), 55)
        self.assertEqual(entance(20), 6765)

    def test_negative_numbers(self):
        with self.assertRaises(ValueError):
            entance(-1)

if __name__ == '__main__':
    unittest.main()