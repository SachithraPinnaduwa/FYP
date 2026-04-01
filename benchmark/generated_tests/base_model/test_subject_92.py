import unittest

class TestFindMaxAdjacentFloors(unittest.TestCase):

    def test_single_floor(self):
        self.assertEqual(find_max_adjacent_floors(2), (1, 1))

    def test_two_floors(self):
        self.assertEqual(find_max_adjacent_floors(3), (1, 2))

    def test_five_floors(self):
        self.assertEqual(find_max_adjacent_floors(15), (1, 5))

    def test_sixteen_floors(self):
        self.assertEqual(find_max_adjacent_floors(16), (16, 1))

    def test_large_budget(self):
        self.assertEqual(find_max_adjacent_floors(9699690), (16, 4389))

    def test_odd_budget(self):
        self.assertEqual(find_max_adjacent_floors(223092870), (129, 20995))

    def test_prime_budget(self):
        self.assertEqual(find_max_adjacent_floors(847288609), (4112949, 206))

    def test_consecutive_sum(self):
        self.assertEqual(find_max_adjacent_floors(900660121), (15006, 30011))

    def test_largest_possible_input(self):
        self.assertEqual(find_max_adjacent_floors(987698769), (46887, 17718))

    def test_maximum_number_of_floors(self):
        self.assertEqual(find_max_adjacent_floors(999999999), (163837, 5994))

if __name__ == '__main__':
    unittest.main()