from subject_4 import *

import unittest

class TestMakePalindromeByInsertion(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(make_palindrome_by_insertion("revive"), "reviver")
        self.assertEqual(make_palindrome_by_insertion("ee"), "eye")
        self.assertEqual(make_palindrome_by_insertion("kitayuta"), "NA")

if __name__ == '__main__':
    unittest.main()