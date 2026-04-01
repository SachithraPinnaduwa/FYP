import unittest

class TestMaxTowerHeight(unittest.TestCase):

    def test_case_1(self):
        n = 3
        rings = [
            (1, 5, 1),
            (2, 6, 2),
            (3, 7, 3)
        ]
        expected_output = 6
        self.assertEqual(max_tower_height(n, rings), expected_output)

    def test_case_2(self):
        n = 4
        rings = [
            (1, 2, 1),
            (1, 3, 3),
            (4, 6, 2),
            (5, 7, 1)
        ]
        expected_output = 4
        self.assertEqual(max_tower_height(n, rings), expected_output)

    def test_case_3(self):
        n = 5
        rings = [
            (1, 3, 1),
            (2, 4, 2),
            (3, 5, 3),
            (4, 6, 4),
            (5, 7, 5)
        ]
        expected_output = 15
        self.assertEqual(max_tower_height(n, rings), expected_output)

    def test_case_4(self):
        n = 1
        rings = [
            (1, 2, 1)
        ]
        expected_output = 1
        self.assertEqual(max_tower_height(n, rings), expected_output)

    def test_case_5(self):
        n = 10
        rings = [
            (1, 2, 1),
            (2, 3, 2),
            (3, 4, 3),
            (4, 5, 4),
            (5, 6, 5),
            (6, 7, 6),
            (7, 8, 7),
            (8, 9, 8),
            (9, 10, 9),
            (10, 11, 10)
        ]
        expected_output = 55
        self.assertEqual(max_tower_height(n, rings), expected_output)

    def test_case_6(self):
        n = 100000
        rings = [
            (1, 2, 1) for _ in range(n)
        ]
        expected_output = n
        self.assertEqual(max_tower_height(n, rings), expected_output)

if __name__ == '__main__':
    unittest.main()