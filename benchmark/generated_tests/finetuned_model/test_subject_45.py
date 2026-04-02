import unittest

def format_repeated_string(string, n):
    return '"{}" repeated {} times is: "{}"'.format(string, n, string * n)

class TestFormatRepeatedString(unittest.TestCase):
    def test_repeater(self):
        self.assertEqual(format_repeater('yo', 3), '"yo" repeated 3 times is: "yoyoyo"')
        self.assertEqual(format_repeater('WuB', 6), '"WuB" repeated 6 times is: "WuBWuBWuBWuBWuBWuB"')
        self.assertEqual(format_repeater('a', 0), '"a" repeated 0 times is: ""')
        self.assertEqual(format_repeater('', 5), '"" repeated 5 times is: ""')
        self.assertEqual(format_repeater('Hello, World!', 2), '"Hello, World!" repeated 2 times is: "Hello, World!Hello, World!"')
        self.assertEqual(format_repeater('123', 4), '"123" repeated 4 times is: "123123123123"')

if __name__ == '__main__':
    unittest.main()