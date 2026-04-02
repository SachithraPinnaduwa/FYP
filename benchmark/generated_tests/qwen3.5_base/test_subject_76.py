import unittest

class TestMaxTowerHeight(unittest.TestCase):
    def test_case_1(self):
        n = 3
        rings = [(1, 2, 1), (2, 3, 2), (3, 1, 3)]
        self.assertEqual(max_tower_height(n, rings), 6)
    
    def test_case_2(self):
        n = 4
        rings = [(1, 2, 1), (2, 3, 2), (3, 4, 3), (4, 1, 4)]
        self.assertEqual(max_tower_height(n, rings), 10)
    
    def test_case_3(self):
        n = 5
        rings = [(1, 2, 1), (2, 3, 2), (3, 4, 3), (4, 5, 4), (5, 1, 5)]
        self.assertEqual(max_tower_height(n, rings), 15)
    
    def test_case_4(self):
        n = 2
        rings = [(1, 2, 1), (2, 1, 2)]
        self.assertEqual(max_tower_height(n, rings), 3)
    
    def test_case_5(self):
        n = 1
        rings = [(1, 1, 1)]
        self.assertEqual(max_tower_height(n, rings), 1)
    
    def test_case_6(self):
        n = 3
        rings = [(1, 2, 1), (2, 3, 2), (3, 1, 3)]
        self.assertEqual(max_tower_height(n, rings), 6)
    
    def test_case_7(self):
        n = 4
        rings = [(1, 2, 1), (2, 3, 2), (3, 4, 3), (4, 1, 4)]
        self.assertEqual(max_tower_height(n, rings), 10)
    
    def test_case_8(self):
        n = 5
        rings = [(1, 2, 1), (2, 3, 2), (3, 4, 3), (4, 5, 4), (5, 1, 5)]
        self.assertEqual(max_tower_height(n, rings), 15)
    
    def test_case_9(self):
        n = 2
        rings = [(1, 2, 1), (2, 1, 2)]
        self.assertEqual(max_tower_height(n, rings), 3)
    
    def test_case_10(self):
        n = 1
        rings = [(1, 1, 1)]
        self.assertEqual(max_tower_height(n, rings), 1)

if __name__ == '__main__':
    unittest.main()
