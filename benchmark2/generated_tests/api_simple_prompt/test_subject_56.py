from subject_56 import *

import unittest

def generate_pattern(n):
    if n <= 0:
        return ""
    return '\n'.join((''.join((str(i) for i in range(n, j, -1))) for j in range(n - 1, -1, -1)))

class TestGeneratePattern(unittest.TestCase):
    def test_pattern_with_positive_integer(self):
        self.assertEqual(generate_pattern(4), "4\n43\n432\n4321")
        self.assertEqual(generate_pattern(6), "6\n65\n654\n6543\n65432\n654321")

    def test_pattern_with_zero(self):
        self.assertEqual(generate_pattern(0), "")

    def test_pattern_with_negative_integer(self):
        self.assertEqual(generate_pattern(-3), "")

if __name__ == '__main__':
    unittest.main()