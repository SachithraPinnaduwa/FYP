from subject_94 import *

import unittest

def calculate_robot_locations(n: int) -> int:
    if n % 2 == 0:
        return int((n - n / 2 + 1) ** 2)
    else:
        return int((n + 2) * ((n + 2) // 2) + (n + 2) // 2)

class TestCalculateRobotLocations(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual(calculate_robot_locations(5), 12)

    def test_edge_case_min_n(self):
        self.assertEqual(calculate_robot_locations(1), 4)

    def test_edge_case_max_n(self):
        self.assertEqual(calculate_robot_locations(1000), 500500)

    def test_error_handling_negative_n(self):
        self.assertEqual(calculate_robot_locations(-1), 0)

if __name__ == '__main__':
    unittest.main()