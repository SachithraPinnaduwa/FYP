import unittest

class TestMineGold(unittest.TestCase):
    def test_mine_gold(self):
        # Test case 1: Multiple gold mines with varying distances from the central hub
        goldMines1 = {
            'mine1': (10, 10),
            'mine2': (30, 30),
            'mine3': (20, 20),
            'mine4': (40, 40)
        }
        centralHub1 = (25, 25)
        expectedOutput1 = (20, 50)
        self.assertEqual(mine_gold(goldMines1, centralHub1), expectedOutput1)

        # Test case 2: Gold mines too close to the central hub
        goldMines2 = {
            'mine1': (10, 10),
            'mine2': (15, 15),
            'mine3': (20, 20)
        }
        centralHub2 = (25, 25)
        expectedOutput2 = (0, 0)
        self.assertEqual(mine_gold(goldMines2, centralHub2), expectedOutput2)

        # Test case 3: Only one gold mine within the minimum distance
        goldMines3 = {
            'mine1': (30, 30)
        }
        centralHub3 = (50, 50)
        expectedOutput3 = (10, 40)
        self.assertEqual(mine_gold(goldMines3, centralHub3), expectedOutput3)

        # Test case 4: Empty gold mines dictionary
        goldMines4 = {}
        centralHub4 = (0, 0)
        expectedOutput4 = (0, 0)
        self.assertEqual(mine_gold(goldMines4, centralHub4), expectedOutput4)

        # Test case 5: Central hub exactly at the same coordinates as a gold mine
        goldMines5 = {
            'mine1': (0, 0)
        }
        centralHub5 = (0, 0)
        expectedOutput5 = (0, 0)
        self.assertEqual(mine_gold(goldMines5, centralHub5), expectedOutput5)

if __name__ == '__main__':
    unittest.main()