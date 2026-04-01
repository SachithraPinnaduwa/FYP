import unittest

class TestRobotLocations(unittest.TestCase):

    def test_single_step(self):
        # Test case for a single step
        self.assertEqual(calculate_robot_locations(1), 4)

    def test_two_steps(self):
        # Test case for two steps
        self.assertEqual(calculate_robot_locations(2), 4)

    def test_three_steps(self):
        # Test case for three steps
        self.assertEqual(calculate_robot_locations(3), 12)

    def test_even_steps(self):
        # Test case for an even number of steps
        self.assertEqual(calculate_robot_locations(4), 9)

    def test_large_steps(self):
        # Test case for a large number of steps
        self.assertEqual(calculate_robot_locations(1000), 500500)

    def test_zero_steps(self):
        # Test case for zero steps (edge case)
        self.assertEqual(calculate_robot_locations(0), 1)