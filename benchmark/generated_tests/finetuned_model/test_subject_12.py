import unittest

def entance(n):
    if n <= 1:
       return n
    else:
       return (entance(n-1) + entance(n-2))

class TestEntranceFunction(unittest.TestCase):
    def test_base_cases(self):
        self.assertEqual(entance(0), 0)
        self.assertEqual(entance(1), 1)

    def test_small_values(self):
        self.assertEqual(entance(2), 1)
        self.assertEqual(entance(3), 2)
        self.assertEqual(entance(4), 3)

    def test_large_values(self):
        self.assertEqual(entance(10), 55)
        self.assertEqual(entance(20), 6765)
        self.assertEqual(entance(30), 832040)

    def test_negative_values(self):
        with self.assertRaises(ValueError):
            entance(-1)
        with self.assertRaises(ValueError):
            entance(-5)

if __name__ == '__main__':
    unittest.main()