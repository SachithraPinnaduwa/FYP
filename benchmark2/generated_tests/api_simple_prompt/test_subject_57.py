from subject_57 import *

import unittest

def filter_strings(data, n):
    result = []
    for string in data:
        if len(string) > n and any(char.isupper() for char in string):
            result.append(string)
    return result

class TestFilterStrings(unittest.TestCase):
    def test_filter_strings(self):
        self.assertEqual(filter_strings(["hello", "world", "Python", "is", "awesome"], 3), ["Python", "awesome"])
        self.assertEqual(filter_strings(["apple", "banana", "cherry", "date"], 4), ["banana", "cherry"])
        self.assertEqual(filter_strings(["123", "4567", "890", "12345"], 5), ["12345"])
        self.assertEqual(filter_strings(["a", "b", "c", "d"], 1), [])
        self.assertEqual(filter_strings(["ABC", "def", "GHI", "jkl"], 2), ["ABC", "GHI"])

if __name__ == '__main__':
    unittest.main()