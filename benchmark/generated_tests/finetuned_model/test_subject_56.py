import unittest

class TestPatternGenerator(unittest.TestCase):

    # Test case for n = 0, which should return an empty string
    def test_n_zero(self):
        self.assertEqual(generate_pattern(0), "")

    # Test case for n = 1, which should return "1"
    def test_n_one(self):
        self.assertEqual(generate_pattern(1), "1")

    # Test case for n = 2, which should return "2\n21"
    def test_n_two(self):
        self.assertEqual(generate_pattern(2), "2\n21")

    # Test case for n = 3, which should return "3\n32\n321"
    def test_n_three(self):
        self.assertEqual(generate_pattern(3), "3\n32\n321")

    # Test case for n = 4, which should return the pattern specified in the problem description
    def test_n_four(self):
        self.assertEqual(generate_pattern(4), "4\n43\n432\n4321")

    # Test case for n = 5, which should return the pattern specified in the problem description
    def test_n_five(self):
        self.assertEqual(generate_pattern(5), "5\n54\n543\n5432\n54321")

    # Test case for n = 6, which should return the pattern specified in the problem description
    def test_n_six(self):
        self.assertEqual(generate_pattern(6), "6\n65\n654\n6543\n65432\n654321")

    # Test case for negative n, which should return an empty string
    def test_negative_n(self):
        self.assertEqual(generate_pattern(-5), "")

    # Test case for n = 10, which should return the pattern for n = 10
    def test_n_ten(self):
        expected_output = "10\n109\n1098\n10987\n109876\n1098765\n10987654\n109876543\n1098765432\n10987654321"
        self.assertEqual(generate_pattern(10), expected_output)