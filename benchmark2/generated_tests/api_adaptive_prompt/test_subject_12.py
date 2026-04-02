from subject_12 import *

import unittest

def entance(n):
    if n <= 1:
       return n
    else:
       return (entance(n-1) + entance(n-2))

class TestEntanceFunction(unittest.TestCase):
    def test_normal_case_positive_integer(self):
        self.assertEqual(entance(5), 5)

    def test_normal_case_zero(self):
        self.assertEqual(entance(0), 0)

    def test_normal_case_one(self):
        self.assertEqual(entance(1), 1)

    def test_edge_case_negative_integer(self):
        with self.assertRaises(ValueError):
            entance(-1)

    def test_error_handling_non_integer_input(self):
        with self.assertRaises(TypeError):
            entance('a')

if __name__ == '__main__':
    unittest.main()