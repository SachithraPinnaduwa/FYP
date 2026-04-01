import unittest

class TestRobotLocations(unittest.TestCase):
    def test_calculate_robot_locations(self):
        self.assertEqual(calculate_robot_locations(1), 4)
        self.assertEqual(calculate_robot_locations(2), 4)
        self.assertEqual(calculate_robot_locations(3), 12)
        self.assertEqual(calculate_robot_locations(4), 16)
        self.assertEqual(calculate_robot_locations(5), 28)
        self.assertEqual(calculate_robot_locations(6), 36)
        self.assertEqual(calculate_robot_locations(7), 52)
        self.assertEqual(calculate_robot_locations(8), 64)
        self.assertEqual(calculate_robot_locations(9), 80)
        self.assertEqual(calculate_robot_locations(10), 100)

if __name__ == '__main__':
    unittest.main()