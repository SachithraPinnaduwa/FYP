from subject_92 import *

import unittest

class TestFindMaxAdjacentFloors(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(find_max_adjacent_floors(15), (1, 5))
        self.assertEqual(find_max_adjacent_floors(16), (16, 1))
        self.assertEqual(find_max_adjacent_floors(2), (2, 1))
        self.assertEqual(find_max_adjacent_floors(3), (1, 2))
        self.assertEqual(find_max_adjacent_floors(9699690), (16, 4389))
        self.assertEqual(find_max_adjacent_floors(223092870), (129, 20995))
        self.assertEqual(find_max_adjacent_floors(847288609), (4112949, 206))
        self.assertEqual(find_max_adjacent_floors(900660121), (15006, 30011))
        self.assertEqual(find_max_adjacent_floors(987698769), (46887, 17718))
        self.assertEqual(find_max_adjacent_floors(999999999), (163837, 5994))

if __name__ == '__main__':
    unittest.main()