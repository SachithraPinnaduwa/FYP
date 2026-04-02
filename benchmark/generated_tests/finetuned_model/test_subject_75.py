import unittest

class TestReverseArray(unittest.TestCase):
    def test_reverseArray(self):
        self.assertEqual(reverseArray([1, 2, 3, 4, 5], 0, 4), None)
        self.assertEqual(reverseArray(['a', 'b', 'c', 'd'], 0, 3), None)
        self.assertEqual(reverseArray([10, 20, 30], 0, 2), None)
        self.assertEqual(reverseArray([1], 0, 0), None)
        self.assertEqual(reverseArray([1, 2, 3, 4, 5, 6], 1, 4), None)
        self.assertEqual(reverseArray([7, 8, 9, 10, 11, 12, 13], 2, 5), None)
        self.assertEqual(reverseArray([0, 0, 0, 0], 0, 3), None)
        self.assertEqual(reverseArray([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 7), None)

if __name__ == '__main__':
    unittest.main()