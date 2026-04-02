from subject_45 import *

import unittest

class TestFormatRepeatedString(unittest.TestCase):
    def test_format_repeated_string(self):
        self.assertEqual(format_repeated_string('yo', 3), '"yo" repeated 3 times is: "yoyoyo"')
        self.assertEqual(format_repeated_string('WuB', 6), '"WuB" repeated 6 times is: "WuBWuBWuBWuBWuBWuB"')
        self.assertEqual(format_repeated_string('a', 0), '"a" repeated 0 times is: ""')
        self.assertEqual(format_repeated_string('', 5), '"" repeated 5 times is: ""')
        self.assertEqual(format_repeated_string('hello', 1), '"hello" repeated 1 times is: "hello"')

if __name__ == '__main__':
    unittest.main()