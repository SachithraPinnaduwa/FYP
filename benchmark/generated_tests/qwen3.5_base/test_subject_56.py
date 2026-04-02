import unittest

class TestGeneratePattern(unittest.TestCase):
    def test_generate_pattern(self):
        self.assertEqual(generate_pattern(5),
            '54321\n4321\n321\n21\n1')
        self.assertEqual(generate_pattern(3),
            '321\n21\n1')
        self.assertEqual(generate_pattern(1),
            '1')
        self.assertEqual(generate_pattern(0),
            '')
        self.assertEqual(generate_pattern(-1),
            '')
        self.assertEqual(generate_pattern(10),
            '10987654321\n987654321\n87654321\n7654321\n654321\n54321\n4321\n321\n21\n1')

if __name__ == '__main__':
    unittest.main()
