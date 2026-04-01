import unittest

class TestMaxMarksWithForgetfulness(unittest.TestCase):

    def test_case_1(self):
        chapters = [(1, 1), (2, 1)]
        total_time = 2
        expected_output = 2
        self.assertEqual(max_marks_with_forgetfulness(chapters, total_time), expected_output)

    def test_case_2(self):
        chapters = [(1, 1), (2, 2)]
        total_time = 3
        expected_output = 2
        self.assertEqual(max_marks_with_forgetfulness(chapters, total_time), expected_output)

    def test_case_3(self):
        chapters = [(3, 3), (4, 2), (5, 3)]
        total_time = 5
        expected_output = 9
        self.assertEqual(max_marks_with_forgetfulness(chapters, total_time), expected_output)

    def test_case_4(self):
        chapters = [(5, 6), (4, 2), (3, 3)]
        total_time = 5
        expected_output = 8
        self.assertEqual(max_marks_with_forgetfulness(chapters, total_time), expected_output)

    def test_case_5(self):
        chapters = [(2, 4), (1, 5)]
        total_time = 1
        expected_output = 0
        self.assertEqual(max_marks_with_forgetfulness(chapters, total_time), expected_output)

if __name__ == '__main__':
    unittest.main()