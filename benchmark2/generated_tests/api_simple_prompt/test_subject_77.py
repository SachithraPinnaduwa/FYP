from subject_77 import *

import unittest
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
    def test_mine_gold(self):
        self.assertEqual(mine_gold({'mine1': (10, 10), 'mine2': (30, 30), 'mine3': (50, 50)}, (20, 20)), (20, 40.0))
        self.assertEqual(mine_gold({'mine1': (10, 10), 'mine2': (30, 30), 'mine3': (50, 50)}, (10, 10)), (10, 20.0))
        self.assertEqual(mine_gold({'mine1': (10, 10), 'mine2': (30, 30), 'mine3': (50, 50)}, (50, 50)), (10, 20.0))
        self.assertEqual(mine_gold({'mine1': (10, 10), 'mine2': (30, 30), 'mine3': (50, 50)}, (40, 40)), (0, 0.0))
        self.assertEqual(mine_gold({'mine1': (10, 10), 'mine2': (30, 30), 'mine3': (50, 50)}, (0, 0)), (0, 0.0))
        self.assertEqual(mine_gold({'mine1': (10, 10), 'mine2': (30, 30), 'mine3': (50, 50)}, (100, 100)), (0, 0.0))
        self.assertEqual(mine_gold({'mine1': (10, 10), 'mine2': (30, 30), 'mine3': (50, 50)}, (25, 25)), (10, 5.0 * math.sqrt(2)))
        self.assertEqual(mine_gold({'mine1': (10, 10), 'mine2': (30, 30), 'mine3': (50, 50)}, (25, 25)), (10, 5.0 * math.sqrt(2)))
        self.assertEqual(mine_gold({'mine1': (10, 10), 'mine2': (30, 30), 'mine3': (50, 50)}, (25, 25)), (10, 5.0 * math.sqrt(2)))
        self.assertEqual(mine_gold({'mine1': (10, 10), 'mine2': (30, 30), 'mine3': (50, 50)}, (25, 25)), (10, 5.0 * math.sqrt(2)))
        self.assertEqual(mine_gold({'mine1': (10, 10), 'mine2': (30, 30), 'mine3': (50, 50)}, (25, 25)), (10, 5.0 * math.sqrt(2)))
        self.assertEqual(mine_gold({'mine1': (10, 10), 'mine2': (30, 30), 'mine3': (50, 50)}, (25, 25)), (10, 5.0 * math.sqrt(2)))
        self.assertEqual(mine_gold({'mine1': (10, 10), 'mine2': (30, 30), 'mine3': (50, 50)}, (25, 25)), (10, 5.0 * math.sqrt(2)))
        self.assertEqual(mine_gold({'mine1': (10, 10), 'mine2': (