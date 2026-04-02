import unittest

class TestMaxMarks(unittest.TestCase):
    def test_case_1(self):
        chapters = [(10, 1), (20, 2), (30, 3)]
        total_time = 5
        self.assertEqual(max_marks_with_forgetfulness(chapters, total_time), 60)

    def test_case_2(self):
        chapters = [(5, 1), (10, 2), (15, 3)]
        total_time = 4
        self.assertEqual(max_marks_with_forgetfulness(chapters, total_time), 25)

    def test_case_3(self):
        chapters = [(100, 10)]
        total_time = 5
        self.assertEqual(max_marks_with_forgetfulness(chapters, total_time), 0)

    def test_case_4(self):
        chapters = [(10, 1), (20, 2), (30, 3), (40, 4)]
        total_time = 7
        self.assertEqual(max_marks_with_forgetfulness(chapters, total_time), 100)

    def test_case_5(self):
        chapters = [(10, 1), (20, 2), (30, 3), (40, 4), (50, 5)]
        total_time = 10
        self.assertEqual(max_marks_with_forgetfulness(chapters, total_time), 150)

if __name__ == '__main__':
    unittest.main()
