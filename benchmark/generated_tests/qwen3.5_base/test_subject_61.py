import unittest

class TestKingMoves(unittest.TestCase):
    def test_king_moves(self):
        # Test case 1: King at (1, 1) with K = 1
        self.assertEqual(count_king_moves(1, 1, 1), 9)
        
        # Test case 2: King at (8, 8) with K = 1
        self.assertEqual(count_king_moves(8, 8, 1), 9)
        
        # Test case 3: King at (4, 4) with K = 1
        self.assertEqual(count_king_moves(4, 4, 1), 9)
        
        # Test case 4: King at (1, 8) with K = 1
        self.assertEqual(count_king_moves(1, 8, 1), 9)
        
        # Test case 5: King at (8, 1) with K = 1
        self.assertEqual(count_king_moves(8, 1, 1), 9)
        
        # Test case 6: King at (1, 1) with K = 2
        self.assertEqual(count_king_moves(1, 1, 2), 16)
        
        # Test case 7: King at (8, 8) with K = 2
        self.assertEqual(count_king_moves(8, 8, 2), 16)
        
        # Test case 8: King at (4, 4) with K = 2
        self.assertEqual(count_king_moves(4, 4, 2), 16)
        
        # Test case 9: King at (1, 8) with K = 2
        self.assertEqual(count_king_moves(1, 8, 2), 16)
        
        # Test case 10: King at (8, 1) with K = 2
        self.assertEqual(count_king_moves(8, 1, 2), 16)
        
        # Test case 11: King at (1, 1) with K = 3
        self.assertEqual(count_king_moves(1, 1, 3), 25)
        
        # Test case 12: King at (8, 8) with K = 3
        self.assertEqual(count_king_moves(8, 8, 3), 25)
        
        # Test case 13: King at (4, 4) with K = 3
        self.assertEqual(count_king_moves(4, 4, 3), 25)
        
        # Test case 14: King at (1, 8) with K = 3
        self.assertEqual(count_king_moves(1, 8, 3), 25)
        
        # Test case 15: King at (8, 1) with K = 3
        self.assertEqual(count_king_moves(8, 1, 3), 25)
        
        # Test case 16: King at (1, 1) with K = 4
        self.assertEqual(count_king_moves(1, 1, 4), 36)
        
        # Test case 17: King at (8, 8) with K = 4
        self.assertEqual(count_king_moves(8, 8, 4), 36)
        
        # Test case 18: King at (4, 4) with K = 4
        self.assertEqual(count_king_moves(4, 4, 4), 36)
        
        # Test case 19: King at (1, 8) with K = 4
        self.assertEqual(count_king_moves(1, 8, 4), 36)
        
        # Test case 20: King at (8, 1) with K = 4
        self.assertEqual(count_king_moves(8, 1, 4), 36)
        
        # Test case 21: King at (1, 1) with K = 5
        self.assertEqual(count_king_moves(1, 1, 5), 49)
        
        # Test case 22: King at (8, 8) with K = 5
        self.assertEqual(count_king_moves(8, 8, 5), 49)
        
        # Test case 23: King at (4, 4) with K = 5
        self.assertEqual(count_king_moves(4, 4, 5), 49)
        
        # Test case 24: King at (1, 8) with K = 5
        self.assertEqual(count_king_moves(1, 8, 5), 49)
        
        # Test case 25: King at (8, 1) with K = 5
        self.assertEqual(count_king_moves(8, 1, 5), 49)
        
        # Test case 26: King at (1, 1) with K = 6
        self.assertEqual(count_king_moves(1, 1, 6), 64)
        
        # Test case 27: King at (8, 8) with K = 6
        self.assertEqual(count_king_moves(8, 8, 6), 64)
        
        # Test case 28: King at (4, 4) with K = 6
        self.assertEqual(count_king_moves(4, 4, 6), 64)
        
        # Test case 29: King at (1, 8) with K = 6
        self.assertEqual(count_king_moves(1, 8, 6), 64)
        
        # Test case 30: King at (8, 1) with K = 6
        self.assertEqual(count_king_moves(8, 1, 6), 64)
        
        # Test case 31: King at (1, 1) with K = 7
        self.assertEqual(count_king_moves(1, 1, 7), 81)
        
        # Test case 32: King at (8, 8) with K = 7
        self.assertEqual(count_king_moves(8, 8, 7), 81)
        
        # Test case 33: King at (4, 4) with K = 7
        self.assertEqual(count_king_moves(4, 4, 7), 81)
        
        # Test case 34: King at (1, 8) with K = 7
        self.assertEqual(count_king_moves(1, 8, 7), 81)
        
        # Test case 35: King at (8, 1) with K = 7
        self.assertEqual(count_king_moves(8, 1, 7