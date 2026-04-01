import unittest

class TestFibonacci(unittest.TestCase):

    def test_base_cases(self):
        self.assertEqual(entrance(0), 0)
        self.assertEqual(entrance(1), 1)

    def test_small_numbers(self):
        self.assertEqual(entrance(2), 1)
        self.assertEqual(entrance(3), 2)
        self.assertEqual(entrance(4), 3)

    def test_larger_numbers(self):
        self.assertEqual(entrance(5), 5)
        self.assertEqual(entrance(6), 8)
        self.assertEqual(entrance(7), 13)
        self.assertEqual(entrance(8), 21)
        self.assertEqual(entrance(9), 34)
        self.assertEqual(entrance(10), 55)

    def test_negative_numbers(self):
        with self.assertRaises(ValueError):
            entrance(-1)
        with self.assertRaises(ValueError):
            entrance(-5)

    def test_large_number(self):
        self.assertEqual(entrance(20), 6765)

if __name__ == '__main__':
    unittest.main()