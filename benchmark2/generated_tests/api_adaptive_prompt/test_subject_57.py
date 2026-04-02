from subject_57 import *

import unittest

class TestFilterStrings(unittest.TestCase):
    def test_filter_strings(self):
        self.assertEqual(filter_strings(["hello", "world", "Python", "code"], 3), ["Python"])
        self.assertEqual(filter_strings(["apple", "banana", "cherry", "date"], 5), ["banana", "cherry"])
        self.assertEqual(filter_strings(["a", "ab", "abc", "abcd"], 2), ["abc", "abcd"])
        self.assertEqual(filter_strings(["123", "4567", "890", "12345"], 3), ["4567", "12345"])
        self.assertEqual(filter_strings(["test", "TEST", "teSt", "tEsT"], 2), ["TEST", "teSt", "tEsT"])

if __name__ == '__main__':
    unittest.main()