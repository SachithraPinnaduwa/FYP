import unittest

def generate_pattern(n):
    if n <= 0:
        return ""
    return '\n'.join((''.join((str(i) for i in range(n, j, -1))) for j in range(n - 1, -1, -1)))

class TestGeneratePattern(unittest.TestCase):
    def test_zero_or_negative_input(self):
        self.assertEqual(generate_pattern(0), "")
        self.assertEqual(generate_pattern(-5), "")
        self.assertEqual(generate_pattern(-1), "")
    
    def test_single_row_pattern(self):
        self.assertEqual(generate_pattern(1), "1")
    
    def test_two_row_pattern(self):
        self.assertEqual(generate_pattern(2), "2\n12")
    
    def test_three_row_pattern(self):
        self.assertEqual(generate_pattern(3), "3\n23\n123")
    
    def test_four_row_pattern(self):
        self.assertEqual(generate_pattern(4), "4\n34\n234\n1234")
    
    def test_six_row_pattern(self):
        self.assertEqual(generate_pattern(6), "6\n56\n456\n3456\n23456\n123456")

if __name__ == '__main__':
    unittest.main()