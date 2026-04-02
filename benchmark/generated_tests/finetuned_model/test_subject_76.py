import unittest

class TestMaxTowerHeight(unittest.TestCase):
    def test_max_tower_height(self):
        self.assertEqual(max_tower_height(3, [(1, 5, 1), (2, 6, 2), (3, 7, 3)]), 6)
        self.assertEqual(max_tower_height(4, [(1, 2, 1), (1, 3, 3), (4, 6, 2), (5, 7, 1)]), 4)
        self.assertEqual(max_tower_height(1, [(1, 10, 10)]), 10)
        self.assertEqual(max_tower_height(2, [(1, 5, 1), (3, 7, 3)]), 4)
        self.assertEqual(max_tower_height(5, [(1, 3, 2), (2, 4, 1), (3, 5, 3), (4, 6, 2), (5, 7, 1)]), 6)

if __name__ == '__main__':
    unittest.main()