import unittest

class TestMaxMarksWithForgetfulness(unittest.TestCase):
    
    def test_base_case(self):
        # Test with the first sample input
        chapters = [(1, 1), (2, 1)]
        total_time = 2
        self.assertEqual(max_marks_with_forgetfulness(chapters, total_time), 2)
        
    def test_base_case_2(self):
        # Test with the second sample input
        chapters = [(1, 1), (2, 2), (3, 3)]
        total_time = 3
        self.assertEqual(max_marks_with_forgetfulness(chapters, total_time), 2)
        
    def test_base_case_3(self):
        # Test with the third sample input
        chapters = [(5, 1), (4, 2), (3, 3), (2, 4), (1, 5)]
        total_time = 6
        self.assertEqual(max_marks_with_forgetfulness(chapters, total_time), 9)
        
    def test_single_chapter(self):
        # Test with a single chapter
        chapters = [(10, 5)]
        total_time = 5
        self.assertEqual(max_marks_with_forgetfulness(chapters, total_time), 10)
        
    def test_no_time_left(self):
        # Test with no time left
        chapters = [(1, 1), (2, 2), (3, 3)]
        total_time = 0
        self.assertEqual(max_marks_with_forgetfulness(chapters, total_time), 0)
        
    def test_no_chapters(self):
        # Test with no chapters
        chapters = []
        total_time = 5
        self.assertEqual(max_marks_with_forgetfulness(chapters, total_time), 0)
        
    def test_large_input(self):
        # Test with a large input
        chapters = [(i, i) for i in range(1, 1001)]
        total_time = 5000
        self.assertEqual(max_marks_with_forgetfulness(chapters, total_time), 1000000)
        
    def test_large_total_time(self):
        # Test with a large total time
        chapters = [(1, 1), (2, 2), (3, 3)]
        total_time = 10000
        self.assertEqual(max_marks_with_forgetfulness(chapters, total_time), 2)