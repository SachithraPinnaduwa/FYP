import unittest

class TestFindMaxAdjacentFloors(unittest.TestCase):
    def test_find_max_adjacent_floors(self):
        # Test case 1: Budget of 100
        self.assertEqual(find_max_adjacent_floors(100), (1, 100))
        # Test case 2: Budget of 1000
        self.assertEqual(find_max_adjacent_floors(1000), (1, 1000))
        # Test case 3: Budget of 10000
        self.assertEqual(find_max_adjacent_floors(10000), (1, 10000))
        # Test case 4: Budget of 100000
        self.assertEqual(find_max_adjacent_floors(100000), (1, 100000))
        # Test case 5: Budget of 1000000
        self.assertEqual(find_max_adjacent_floors(1000000), (1, 1000000))
        # Test case 6: Budget of 10000000
        self.assertEqual(find_max_adjacent_floors(10000000), (1, 10000000))
        # Test case 7: Budget of 100000000
        self.assertEqual(find_max_adjacent_floors(100000000), (1, 100000000))
        # Test case 8: Budget of 1000000000
        self.assertEqual(find_max_adjacent_floors(1000000000), (1, 1000000000))
        # Test case 9: Budget of 10000000000
        self.assertEqual(find_max_adjacent_floors(10000000000), (1, 10000000000))
        # Test case 10: Budget of 100000000000
        self.assertEqual(find_max_adjacent_floors(100000000000), (1, 100000000000))
        # Test case 11: Budget of 1000000000000
        self.assertEqual(find_max_adjacent_floors(1000000000000), (1, 1000000000000))
        # Test case 12: Budget of 10000000000000
        self.assertEqual(find_max_adjacent_floors(10000000000000), (1, 10000000000000))
        # Test case 13: Budget of 100000000000000
        self.assertEqual(find_max_adjacent_floors(100000000000000), (1, 100000000000000))
        # Test case 14: Budget of 1000000000000000
        self.assertEqual(find_max_adjacent_floors(1000000000000000), (1, 1000000000000000))
        # Test case 15: Budget of 10000000000000000
        self.assertEqual(find_max_adjacent_floors(10000000000000000), (1, 10000000000000000))
        # Test case 16: Budget of 100000000000000000
        self.assertEqual(find_max_adjacent_floors(100000000000000000), (1, 100000000000000000))
        # Test case 17: Budget of 1000000000000000000
        self.assertEqual(find_max_adjacent_floors(1000000000000000000), (1, 1000000000000000000))
        # Test case 18: Budget of 10000000000000000000
        self.assertEqual(find_max_adjacent_floors(10000000000000000000), (1, 10000000000000000000))
        # Test case 19: Budget of 100000000000000000000
        self.assertEqual(find_max_adjacent_floors(100000000000000000000), (1, 100000000000000000000))
        # Test case 20: Budget of 1000000000000000000000
        self.assertEqual(find_max_adjacent_floors(1000000000000000000000), (1, 1000000000000000000000))
        # Test case 21: Budget of 10000000000000000000000
        self.assertEqual(find_max_adjacent_floors(10000000000000000000000), (1, 10000000000000000000000))
        # Test case 22: Budget of 100000000000000000000000
        self.assertEqual(find_max_adjacent_floors(100000000000000000000000),