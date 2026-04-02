from subject_91 import *

import unittest

def reverse_string(s):
    # Convert the string to a list since strings are immutable
    s = list(s)
    start = 0
    end = len(s) - 1
    
    # Iterate until start is less than end
    while start < end:
        # Swap characters at start and end
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1
    
    # Convert the list back to a string
    return ''.join(s)

class TestReverseString(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string("world"), "dlrow")
        self.assertEqual(reverse_string("Python"), "nohtyP")
        self.assertEqual(reverse_string(""), "")
        self.assertEqual(reverse_string("a"), "a")
        self.assertEqual(reverse_string("ab"), "ba")

if __name__ == '__main__':
    unittest.main()