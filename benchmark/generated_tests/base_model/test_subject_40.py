import unittest

class TestMinIncrementOperations(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(min_increment_operations([1, 2, 2], 3), 1)

    def test_case_2(self):
        self.assertEqual(min_increment_operations([1, 1, 2, 3], 4), 3)

    def test_case_3(self):
        self.assertEqual(min_increment_operations([1, 2, 3, 4, 5], 5), 0)

    def test_case_4(self):
        self.assertEqual(min_increment_operations([10, 20, 30, 40, 50], 5), 0)

    def test_case_5(self):
        self.assertEqual(min_increment_operations([1, 1, 1, 1, 1], 5), 10)

    def test_case_6(self):
        self.assertEqual(min_increment_operations([5, 3, 5, 2, 3, 3, 9, 0, 123], 9), 17)

    def test_case_7(self):
        self.assertEqual(min_increment_operations([10**9, 10**9, 10**9], 3), 2*10**9)

if __name__ == '__main__':
    unittest.main()