import unittest

class TestRobotLocations(unittest.TestCase):
    def test_even_n(self):
        self.assertEqual(calculate_robot_locations(4), 9)
        self.assertEqual(calculate_robot_locations(6), 16)
        self.assertEqual(calculate_robot_locations(8), 25)
    
    def test_odd_n(self):
        self.assertEqual(calculate_robot_locations(3), 10)
        self.assertEqual(calculate_robot_locations(5), 18)
        self.assertEqual(calculate_robot_locations(7), 28)
    
    def test_edge_cases(self):
        self.assertEqual(calculate_robot_locations(1), 4)
        self.assertEqual(calculate_robot_locations(2), 9)
        self.assertEqual(calculate_robot_locations(100), 2500)

if __name__ == '__main__':
    unittest.main()
