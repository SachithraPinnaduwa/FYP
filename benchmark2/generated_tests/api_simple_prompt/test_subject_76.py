from subject_76 import *

import unittest

class TestMaxTowerHeight(unittest.TestCase):
    def test_max_tower_height(self):
        self.assertEqual(max_tower_height(3, [(1, 5, 1), (2, 6, 2), (3, 7, 3)]), 6)
        self.assertEqual(max_tower_height(4, [(1, 2, 1), (1, 3, 3), (4, 6, 2), (5, 7, 1)]), 4)

if __name__ == '__main__':
    unittest.main()