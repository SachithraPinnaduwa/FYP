import unittest

class TestMinIncrementOperations(unittest.TestCase):
    def test_case_1(self):
        arr = [1, 2, 3]
        N = 3
        self.assertEqual(min_increment_operations(arr, N), 0)

    def test_case_2(self):
        arr = [1, 1, 1]
        N = 3
        self.assertEqual(min_increment_operations(arr, N), 2)

    def test_case_3(self):
        arr = [1, 2, 3, 4, 5]
        N = 5
        self.assertEqual(min_increment_operations(arr, N), 0)

    def test_case_4(self):
        arr = [1, 1, 1, 1]
        N = 4
        self.assertEqual(min_increment_operations(arr, N), 3)

    def test_case_5(self):
        arr = [1, 2, 3, 4, 5, 6]
        N = 6
        self.assertEqual(min_increment_operations(arr, N), 0)

    def test_case_6(self):
        arr = [1, 1, 1, 1, 1]
        N = 5
        self.assertEqual(min_increment_operations(arr, N), 4)

    def test_case_7(self):
        arr = [1, 2, 3, 4, 5, 6, 7]
        N = 7
        self.assertEqual(min_increment_operations(arr, N), 0)

    def test_case_8(self):
        arr = [1, 1, 1, 1, 1, 1]
        N = 6
        self.assertEqual(min_increment_operations(arr, N), 5)

    def test_case_9(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8]
        N = 8
        self.assertEqual(min_increment_operations(arr, N), 0)

    def test_case_10(self):
        arr = [1, 1, 1, 1, 1, 1, 1]
        N = 7
        self.assertEqual(min_increment_operations(arr, N), 6)

if __name__ == '__main__':
    unittest.main()
