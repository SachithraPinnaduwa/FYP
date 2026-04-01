import unittest

class TestFibonacci(unittest.TestCase):

    def test_base_cases(self):
        self.assertEqual(entance(0), 0)
        self.assertEqual(entance(1), 1)

    def test_small_values(self):
        self.assertEqual(entance(2), 1)
        self.assertEqual(entance(3), 2)
        self.assertEqual(entance(4), 3)

    def test_larger_values(self):
        self.assertEqual(entance(5), 5)
        self.assertEqual(entance(6), 8)
        self.assertEqual(entance(7), 13)

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            entance(-1)

if __name__ == '__main__':
    unittest.main()