from subject_61 import *

import unittest

def count_king_moves(R, C, K):
    a = min(8, R + K) - max(1, R - K) + 1
    b = min(8, C + K) - max(1, C - K) + 1
    return a * b

class TestCountKingMoves(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(count_king_moves(1, 3, 1), 6)
    
    def test_case_2(self):
        self.assertEqual(count_king_moves(1, 1, 1), 3)
    
    def test_case_3(self):
        self.assertEqual(count_king_moves(8, 8, 1), 3)
    
    def test_case_4(self):
        self.assertEqual(count_king_moves(4, 4, 2), 13)
    
    def test_case_5(self):
        self.assertEqual(count_king_moves(1, 1, 8), 64)
    
    def test_case_6(self):
        self.assertEqual(count_king_moves(8, 8, 8), 64)
    
    def test_case_7(self):
        self.assertEqual(count_king_moves(4, 4, 0), 1)
    
    def test_case_8(self):
        self.assertEqual(count_king_moves(1, 1, 2), 9)
    
    def test_case_9(self):
        self.assertEqual(count_king_moves(8, 8, 2), 9)
    
    def test_case_10(self):
        self.assertEqual(count_king_moves(4, 4, 3), 25)

if __name__ == '__main__':
    unittest.main()