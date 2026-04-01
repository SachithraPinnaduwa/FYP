import unittest

class TestFindMinDeviationShift(unittest.TestCase):

    def test_case_1(self):
        n = 3
        p = [1, 2, 3]
        expected_output = (0, 0)
        self.assertEqual(find_min_deviation_shift(n, p), expected_output)

    def test_case_2(self):
        n = 3
        p = [2, 3, 1]
        expected_output = (0, 1)
        self.assertEqual(find_min_deviation_shift(n, p), expected_output)

    def test_case_3(self):
        n = 3
        p = [3, 2, 1]
        expected_output = (2, 1)
        self.assertEqual(find_min_deviation_shift(n, p), expected_output)

    def test_case_4(self):
        n = 5
        p = [5, 1, 2, 3, 4]
        expected_output = (0, 0)
        self.assertEqual(find_min_deviation_shift(n, p), expected_output)

    def test_case_5(self):
        n = 5
        p = [1, 5, 2, 3, 4]
        expected_output = (2, 1)
        self.assertEqual(find_min_deviation_shift(n, p), expected_output)

    def test_case_6(self):
        n = 5
        p = [5, 2, 3, 4, 1]
        expected_output = (2, 1)
        self.assertEqual(find_min_deviation_shift(n, p), expected_output)

    def test_case_7(self):
        n = 10
        p = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        expected_output = (50, 5)
        self.assertEqual(find_min_deviation_shift(n, p), expected_output)

    def test_case_8(self):
        n = 10
        p = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]
        expected_output = (40, 1)
        self.assertEqual(find_min_deviation_shift(n, p), expected_output)

    def test_case_9(self):
        n = 10
        p = [10, 2, 3, 4, 5, 6, 7, 8, 9, 1]
        expected_output = (40, 1)
        self.assertEqual(find_min_deviation_shift(n, p), expected_output)

if __name__ == '__main__':
    unittest.main()