from subject_94 import *

import unittest

def calculate_robot_locations(n: int) -> int:
    if n % 2 == 0:
        return int((n - n / 2 + 1) ** 2)
    else:
        return int((n + 2) * ((n + 2) // 2) + (n + 2) // 2)

class TestCalculateRobotLocations(unittest.TestCase):
    def test_calculate_robot_locations(self):
        self.assertEqual(calculate_robot_locations(1), 4)
        self.assertEqual(calculate_robot_locations(2), 4)
        self.assertEqual(calculate_robot_locations(3), 12)
        self.assertEqual(calculate_robot_locations(4), 16)
        self.assertEqual(calculate_robot_locations(5), 36)
        self.assertEqual(calculate_robot_locations(6), 36)
        self.assertEqual(calculate_robot_locations(7), 60)
        self.assertEqual(calculate_robot_locations(8), 64)
        self.assertEqual(calculate_robot_locations(9), 100)
        self.assertEqual(calculate_robot_locations(10), 100)

if __name__ == '__main__':
    unittest.main()