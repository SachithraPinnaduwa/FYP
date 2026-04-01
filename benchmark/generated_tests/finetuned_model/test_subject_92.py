import unittest

class TestFindMaxAdjacentFloors(unittest.TestCase):
    def test_base_case(self):
        # Test with a budget that is a perfect square
        self.assertEqual(find_max_adjacent_floors(15), (5, 1))

    def test_budget_equal_to_one(self):
        # Test with a budget of 1 (the smallest possible budget)
        self.assertEqual(find_max_adjacent_floors(1), (1, 1))

    def test_budget_equal_to_two(self):
        # Test with a budget of 2 (the second smallest possible budget)
        self.assertEqual(find_max_adjacent_floors(2), (1, 1))

    def test_budget_with_multiple_floors(self):
        # Test with a budget that can be divided into multiple floors
        self.assertEqual(find_max_adjacent_floors(16), (1, 16))

    def test_budget_with_no_floors(self):
        # Test with a budget that cannot be divided into multiple floors
        self.assertEqual(find_max_adjacent_floors(2), (1, 1))

    def test_budget_with_large_value(self):
        # Test with a large budget
        self.assertEqual(find_max_adjacent_floors(9699690), (4389, 16))

    def test_budget_with_multiple_divisors(self):
        # Test with a budget that has multiple divisors
        self.assertEqual(find_max_adjacent_floors(987698769), (17718, 46887))

    def test_budget_with_no_solution(self):
        # Test with a budget that has no solution
        self.assertEqual(find_max_adjacent_floors(3), (1, 2))