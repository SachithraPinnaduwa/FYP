from subject_17 import *

import unittest

class TestCountBeautifulFences(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(count_beautiful_fences(2, 3, [(1, 2), (2, 3)]), 2)
    
    def test_case_2(self):
        self.assertEqual(count_beautiful_fences(1, 2, [(2, 2)]), 1)
    
    def test_case_3(self):
        self.assertEqual(count_beautiful_fences(6, 6, [(2, 1), (3, 2), (2, 5), (3, 3), (5, 1), (2, 1)]), 20)

if __name__ == '__main__':
    unittest.main()