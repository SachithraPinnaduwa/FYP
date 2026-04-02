import unittest

class TestSolve(unittest.TestCase):
    def test_case_1(self):
        input_list = [3, 1, 2, [4, 2], 5, [3, 1], 6]
        expected_output = [[1, 3], [2, 4], 1, 2, 3, 5, 6]
        self.assertEqual(solve(input_list), expected_output)

    def test_case_2(self):
        input_list = [10, 20, 30, [5, 15], 40, [10, 20], 60]
        expected_output = [[5, 15], [10, 20], 10, 20, 30, 40, 60]
        self.assertEqual(solve(input_list), expected_output)

    def test_case_3(self):
        input_list = [1, 2, 3, [4, 5], 6, [7, 8], 9]
        expected_output = [[4, 5], [7, 8], 1, 2, 3, 6, 9]
        self.assertEqual(solve(input_list), expected_output)

    def test_case_4(self):
        input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected_output = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(solve(input_list), expected_output)

    def test_case_5(self):
        input_list = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
        expected_output = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
        self.assertEqual(solve(input_list), expected_output)

    def test_case_6(self):
        input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, [11, 12], [13, 14], [15, 16]]
        expected_output = [[11, 12], [13, 14], [15, 16], 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(solve(input_list), expected_output)

    def test_case_7(self):
        input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, [11, 12], [13, 14], [15, 16], [17, 18]]
        expected_output = [[11, 12], [13, 14], [15, 16], [17, 18], 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(solve(input_list), expected_output)

    def test_case_8(self):
        input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, [11, 12], [13, 14], [15, 16], [17, 18], [19, 20]]
        expected_output = [[11, 12], [13, 14], [15, 16], [17, 18], [19, 20], 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(solve(input_list), expected_output)

    def test_case_9(self):
        input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, [11, 12], [13, 14], [15, 16], [17, 18], [19, 20], [21, 22]]
        expected_output = [[11, 12], [13, 14], [15, 16], [17, 18], [19, 20], [21, 22], 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(solve(input_list), expected_output)

    def test_case_10(self):
        input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, [11, 12], [13, 14], [15, 16], [17, 18], [19, 20], [21, 22], [23, 24]]
        expected_output = [[11, 12], [13, 14], [15, 16], [17, 18], [19, 20], [21, 22], [23, 24], 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(solve(input_list), expected_output)

if __name__ == '__main__':
    unittest.main()
