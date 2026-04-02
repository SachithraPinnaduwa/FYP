from subject_92 import *

import unittest

def find_max_adjacent_floors(budget):
    """
    Finds the plan with the maximal number of vertically adjacent floors whose total rental cost is exactly equal to the given budget.

    Parameters:
    budget (int): The total rental cost per month.

    Returns:
    tuple: A tuple containing two integers (start_floor, num_floors).
    """
    t = int((budget * 2) ** 0.5) + 1
    for i in range(t, 1, -1):
        if i % 2 == 1:
            if budget % i == 0 and budget // i > i // 2:
                return (budget // i - i // 2, i)
        elif budget % i != 0 and budget * 2 % i == 0 and (budget // i + 1 > i // 2):
            return (budget // i - i // 2 + 1, i)
    return (budget, 1)

class TestFindMaxAdjacentFloors(unittest.TestCase):
    def test_normal_case_1(self):
        self.assertEqual(find_max_adjacent_floors(15), (1, 5))

    def test_normal_case_2(self):
        self.assertEqual(find_max_adjacent_floors(16), (16, 1))

    def test_normal_case_3(self):
        self.assertEqual(find_max_adjacent_floors(2), (2, 1))

    def test_normal_case_4(self):
        self.assertEqual(find_max_adjacent_floors(3), (1, 2))

    def test_normal_case_5(self):
        self.assertEqual(find_max_adjacent_floors(9699690), (16, 4389))

    def test_normal_case_6(self):
        self.assertEqual(find_max_adjacent_floors(223092870), (129, 20995))

    def test_normal_case_7(self):
        self.assertEqual(find_max_adjacent_floors(847288609), (4112949, 206))

    def test_normal_case_8(self):
        self.assertEqual(find_max_adjacent_floors(900660121), (15006, 30011))

    def test_normal_case_9(self):
        self.assertEqual(find_max_adjacent_floors(987698769), (46887, 17718))

    def test_normal_case_10(self):
        self.assertEqual(find_max_adjacent_floors(999999999), (163837, 5994))

if __name__ == '__main__':
    unittest.main()