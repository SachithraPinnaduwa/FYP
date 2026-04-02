from subject_56 import *

import unittest

def generate_pattern(n):
    if n <= 0:
        return ""
    return '\n'.join((''.join((str(i) for i in range(n, j, -1))) for j in range(n - 1, -1, -1)))

class TestGeneratePattern(unittest.TestCase):
    def test_normal_case_with_positive_integer(self):
        self.assertEqual(generate_pattern(5), "5\n54\n543\n5432\n54321")

    def test_normal_case_with_larger_positive_integer(self):
        self.assertEqual(generate_pattern(10), "10\n109\n1098\n10987\n109876\n1098765\n10987654\n109876543\n1098765432\n10987654321")

    def test_edge_case_with_smallest_positive_integer(self):
        self.assertEqual(generate_pattern(1), "1")

    def test_error_handling_with_zero(self):
        self.assertEqual(generate_pattern(0), "")

    def test_error_handling_with_negative_integer(self):
        self.assertEqual(generate_pattern(-5), "")

if __name__ == '__main__':
    unittest.main()