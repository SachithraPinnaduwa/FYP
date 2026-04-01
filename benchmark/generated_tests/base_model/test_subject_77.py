import unittest
from unittest.mock import patch
import math

def mine_gold(goldMines, centralHub):
    goldMines = dict(sorted(goldMines.items(), key=lambda x: math.sqrt((centralHub[0]-x[1][0])**2 + (centralHub[1]-x[1][1])**2)))
    
    totalGold = 0
    distanceTraveled = 0
    for mine in goldMines:
        if math.sqrt((centralHub[0]-goldMines[mine][0])**2 + (centralHub[1]-goldMines[mine][1])**2) >= 20:
            totalGold += 10
            distanceTraveled += math.sqrt((centralHub[0]-goldMines[mine][0])**2 + (centralHub[1]-goldMines[mine][1])**2)
    
    return totalGold, distanceTraveled

class TestMineGold(unittest.TestCase):

    def test_no_mines(self):
        self.assertEqual(mine_gold({}, (0, 0)), (0, 0))

    def test_single_mine_too_close(self):
        self.assertEqual(mine_gold({(5, 5): 1}, (0, 0)), (0, 0))

    def test_single_mine_far_enough(self):
        self.assertEqual(mine_gold({(30, 30): 1}, (0, 0)), (10, math.sqrt(900 + 900)))

    def test_multiple_mines_some_too_close(self):
        self.assertEqual(mine_gold({(5, 5): 1, (30, 30): 1, (45, 45): 1}, (0, 0)), (20, math.sqrt(900 + 900) + math.sqrt(8100 + 8100)))

    def test_multiple_mines_all_far_enough(self):
        self.assertEqual(mine_gold({(30, 30): 1, (45, 45): 1, (60, 60): 1}, (0, 0)), (30, math.sqrt(900 + 900) + math.sqrt(8100 + 8100) + math.sqrt(12100 + 12100)))

if __name__ == '__main__':
    unittest.main()