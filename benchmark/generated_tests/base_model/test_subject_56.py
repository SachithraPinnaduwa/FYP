import unittest

def generate_pattern(n):
    if n <= 0:
        return ""
    return '\n'.join((''.join((str(i) for i in range(n, j, -1))) for j in range(n - 1, -1, -1)))

class TestGeneratePattern(unittest.TestCase):
    def test_negative_input(self):
        self.assertEqual(generate_pattern(-1), "")
        self.assertEqual(generate_pattern(0), "")

    def test_single_row(self):
        self.assertEqual(generate_pattern(1), "1")

    def test_two_rows(self):
        expected_output = "2\n21"
        self.assertEqual(generate_pattern(2), expected_output)

    def test_three_rows(self):
        expected_output = "3\n32\n321"
        self.assertEqual(generate_pattern(3), expected_output)

    def test_four_rows(self):
        expected_output = "4\n43\n432\n4321"
        self.assertEqual(generate_pattern(4), expected_output)

    def test_six_rows(self):
        expected_output = "6\n65\n654\n6543\n65432\n654321"
        self.assertEqual(generate_pattern(6), expected_output)

if __name__ == '__main__':
    unittest.main()