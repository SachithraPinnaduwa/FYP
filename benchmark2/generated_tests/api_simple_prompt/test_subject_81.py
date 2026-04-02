from subject_81 import *

import unittest

class TestFindMinNumber(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(find_min_number("35", "4"), "34")
        self.assertEqual(find_min_number("42", "4"), "24")
        self.assertEqual(find_min_number("24", "9"), "24")

if __name__ == '__main__':
    unittest.main()