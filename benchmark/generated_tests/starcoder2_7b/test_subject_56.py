```
import unittest

class Test(unittest.TestCase):
    def test_generate_pattern(self):
        self.assertEqual(generate_pattern(0), "")
        self.assertEqual(generate_pattern(1), "1")
        self.assertEqual(generate_pattern(2), "2\n21")
        self.assertEqual(generate_pattern(3), "3\n32\n321")
        self.assertEqual(generate_pattern(4), "4\n43\n432\n4321")
        self.assertEqual(generate_pattern(5), "5\n54\n543\n5432\n54321")
        self.assertEqual(generate_pattern(6), "6\n65\n654\n6543\n65432\n654321")
        self.assertEqual(generate_pattern(7), "7\n76\n765\n7654\n76543\n765432\n7654321")
        self.assertEqual(generate_pattern(8), "8\n87\n876\n8765\n87654\n876543\n8765432\n87654321")
        self.assertEqual(generate_pattern(9), "9\n98\n987\n9876\n98765\n987654\n9876543\n98765432\n987654321")
        self.assertEqual(generate_pattern(10), "10\n109\n1098\n10987\n109876\n1098765\n10987654\n109876543\n1098765432\n10987654321")
        self.assertEqual(generate_pattern(11), "11\n1110\n11