import unittest

class TestCountBeautifulFences(unittest.TestCase):
    def test_1(self):
        self.assertEqual(count_beautiful_fences(3, 2, [[1, 2], [2, 3], [3, 1]]), 6)
    def test_2(self):
        self.assertEqual(count_beautiful_fences(3, 2, [[1, 1], [2, 2], [3, 3]]), 3)
    def test_3(self):
        self.assertEqual(count_beautiful_fences(3, 2, [[1, 2], [1, 2], [1, 2]]), 3)
    def test_4(self):
        self.assertEqual(count_beautiful_fences(3, 2, [[1, 1], [1, 1], [1, 1]]), 3)
    def test_5(self):
        self.assertEqual(count_beautiful_fences(3, 2, [[1, 2], [2, 3], [3, 1], [1, 2], [2, 3], [3, 1]]), 12)
    def test_6(self):
        self.assertEqual(count_beautiful_fences(3, 2, [[1, 1], [2, 2], [3, 3], [1, 1], [2, 2], [3, 3]]), 6)
    def test_7(self):
        self.assertEqual(count_beautiful_fences(3, 2, [[1, 2], [2, 3], [3, 1], [1, 2], [2, 3], [3, 1], [1, 2], [2, 3], [3, 1]]), 18)
    def test_8(self):
        self.assertEqual(count_beautiful_fences(3, 2, [[1, 1], [2, 2], [3, 3], [1, 1], [2, 2], [3, 3], [1, 1], [2, 2], [3, 3]]), 9)
    def test_9(self):
        self.assertEqual(count_beautiful_fences(3, 2, [[1, 2], [2, 3], [3, 1], [1, 2], [2, 3], [3, 1], [1, 2], [2, 3], [3, 1], [1, 2], [2, 3], [3, 1]]), 24)
    def test_10(self):
        self.assertEqual(count_beautiful_fences(3, 2, [[1, 1], [2, 2], [3, 3], [1, 1], [2, 2], [3, 3], [1, 1], [2, 2], [3, 3], [1, 1], [2, 2], [3, 3]]), 12)
    def test_11(self):
        self.assertEqual(count_beautiful_fences(3, 2, [[1, 2], [2, 3], [3, 1], [1, 2], [2, 3], [3, 1], [1, 2], [2, 3], [3, 1], [1, 2], [2, 3], [3, 1], [1, 2], [2, 3], [3, 1]]), 30)
    def test_12(self):
        self.assertEqual(count_beautiful_fences(3, 2, [[1, 1], [2, 2], [3, 3], [1, 1], [2, 2], [3, 3], [1, 1], [2, 2], [3, 3], [1, 1], [2, 2], [3, 3], [1, 1], [2, 2], [3, 3]]), 15)
    def test_13(self):
        self.assertEqual(count_beautiful_fences(3, 2, [[1, 2], [2, 3], [3, 1], [1, 2], [2, 3], [3, 1], [1, 2], [2, 3], [3, 1], [1, 2], [2, 3], [3, 1], [1, 2], [2, 3], [3, 1], [1, 2], [2, 3], [3, 1]]), 36)
    def test_14(self):
        self.assertEqual(count_beautiful_fences(3, 2, [[1, 1], [2, 2], [3, 3], [1, 1], [2, 2], [3, 3], [1, 1], [2, 2], [3, 3], [1, 1], [2, 2], [3, 3], [1, 1], [2, 2], [3, 3], [1, 1], [2, 2], [3, 3]]), 18)
    def test_15(self):
        self.assertEqual(count_beautiful_fences(3, 2, [[1, 2], [2, 3], [3, 1], [1, 2], [2, 3], [3, 1], [1, 2], [2, 3], [3, 1], [1, 2], [2, 3], [3, 1], [1, 2], [2, 3], [3, 1], [1, 2], [2, 3], [3, 1], [1, 2], [2, 3], [3, 1]]), 42)
    def test_16(self):
        self.assertEqual(count_beautiful_fences(3, 2, [[1, 1], [2, 2], [3, 3], [1, 1], [2, 2], [3, 3], [1, 1], [2, 2], [3, 3], [1, 1], [2, 2], [3, 3], [1, 1], [2, 2], [3, 3], [1, 1], [2, 2], [3, 3], [1, 1], [2, 2], [3, 3]]), 21)
    def test_17(self):
        self.assertEqual(count_beautiful_fences(3, 2, [[1, 2], [2,