import unittest

class Test(unittest.TestCase):
    def test_count_beautiful_fences(self):
        self.assertEqual(count_beautiful_fences(2, 3, [[1, 2], [2, 3]]), 2)
        self.assertEqual(count_beautiful_fences(1, 2, [[2, 2]]), 1)
        self.assertEqual(count_beautiful_fences(6, 6, [[2, 1], [3, 2], [2, 5], [3, 3], [5, 1], [2, 1]]), 20)

if __name__ == '__main__':
    unittest.main()