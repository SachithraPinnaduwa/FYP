import unittest

class TestCountValidAndPairs(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(count_valid_and_pairs([1, 1, 1, 1, 1]), 10)
    
    def test_case_2(self):
        self.assertEqual(count_valid_and_pairs([10]), 0)
    
    def test_case_3(self):
        self.assertEqual(count_valid_and_pairs([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 45)
    
    def test_case_4(self):
        self.assertEqual(count_valid_and_pairs([1, 2, 3, 4, 5]), 10)
    
    def test_case_5(self):
        self.assertEqual(count_valid_and_pairs([10, 20, 30, 40, 50]), 0)
    
    def test_case_6(self):
        self.assertEqual(count_valid_and_pairs([1, 1, 1, 1]), 6)
    
    def test_case_7(self):
        self.assertEqual(count_valid_and_pairs([2, 4, 6, 8, 10]), 0)
    
    def test_case_8(self):
        self.assertEqual(count_valid_and_pairs([1, 2, 3, 4, 5, 6, 7, 8, 9]), 36)
    
    def test_case_9(self):
        self.assertEqual(count_valid_and_pairs([10, 20, 30, 40]), 0)
    
    def test_case_10(self):
        self.assertEqual(count_valid_and_pairs([1, 1, 1, 1, 1, 1]), 15)

if __name__ == '__main__':
    unittest.main()