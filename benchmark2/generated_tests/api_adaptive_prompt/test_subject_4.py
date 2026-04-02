from subject_4 import *

import unittest

def make_palindrome_by_insertion(s: str) -> str:
    def is_palindrome(n: str) -> bool:
        return n == n[::-1]
    
    for i in range(len(s) + 1):
        for char in 'abcdefghijklmnopqrstuvwxyz':
            new_string = s[:i] + char + s[i:]
            if is_palindrome(new_string):
                return new_string
    
    return "NA"

class TestMakePalindromeByInsertion(unittest.TestCase):
    def test_normal_case_1(self):
        self.assertEqual(make_palindrome_by_insertion("revive"), "reviver")

    def test_normal_case_2(self):
        self.assertEqual(make_palindrome_by_insertion("ee"), "eye")

    def test_normal_case_3(self):
        self.assertEqual(make_palindrome_by_insertion("kitayuta"), "NA")

    def test_edge_case_1(self):
        self.assertEqual(make_palindrome_by_insertion(""), "NA")

    def test_edge_case_2(self):
        self.assertEqual(make_palindrome_by_insertion("a"), "a")

    def test_edge_case_3(self):
        self.assertEqual(make_palindrome_by_insertion("aa"), "aa")

    def test_error_handling_1(self):
        self.assertEqual(make_palindrome_by_insertion("Hello"), "NA")

    def test_error_handling_2(self):
        self.assertEqual(make_palindrome_by_insertion("HELLO"), "NA")

    def test_error_handling_3(self):
        self.assertEqual(make_palindrome_by_insertion("123"), "NA")

if __name__ == '__main__':
    unittest.main()