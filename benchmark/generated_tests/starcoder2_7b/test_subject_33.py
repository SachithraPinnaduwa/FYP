import unittest

class TestMaxMarks(unittest.TestCase):
    def test_max_marks_with_forgetfulness(self):
        self.assertEqual(max_marks_with_forgetfulness([(1, 1), (2, 1)], 2), 2)
        self.assertEqual(max_marks_with_forgetfulness([(1, 1), (2, 1)], 2), 2)
        self.assertEqual(max_marks_with_forgetfulness([(3, 1), (2, 2), (5, 3)], 9), 9)

if __name__ == '__main__':
    unittest.main()