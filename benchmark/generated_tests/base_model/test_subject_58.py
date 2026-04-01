import unittest
from calculate_topocentric_distance import calculate_topocentric_distance

class TestCalculateTopocentricDistance(unittest.TestCase):

    def test_calculate_topocentric_distance(self):
        # Test case 1: Observer at equator, celestial body directly above
        self.assertAlmostEqual(calculate_topocentric_distance(0, 0, 0, 90), 149.6e6, places=2)

        # Test case 2: Observer at north pole, celestial body directly overhead
        self.assertAlmostEqual(calculate_topocentric_distance(90, 0, 0, 0), 149.6e6, places=2)

        # Test case 3: Observer at south pole, celestial body directly overhead
        self.assertAlmostEqual(calculate_topocentric_distance(-90, 0, 0, 0), 149.6e6, places=2)

        # Test case 4: Observer at equator, celestial body at 45 degrees east
        self.assertAlmostEqual(calculate_topocentric_distance(0, 0, 45, 0), 149.6e6 * math.sqrt(2) / 2, places=2)

        # Test case 5: Observer at equator, celestial body at 45 degrees west
        self.assertAlmostEqual(calculate_topocentric_distance(0, 0, -45, 0), 149.6e6 * math.sqrt(2) / 2, places=2)

        # Test case 6: Observer at equator, celestial body at 90 degrees east
        self.assertAlmostEqual(calculate_topocentric_distance(0, 0, 90, 0), 0, places=2)

        # Test case 7: Observer at equator, celestial body at 90 degrees west
        self.assertAlmostEqual(calculate_topocentric_distance(0, 0, -90, 0), 0, places=2)

        # Test case 8: Observer at equator, celestial body at 45 degrees north
        self.assertAlmostEqual(calculate_topocentric_distance(0, 0, 0, 45), 149.6e6 * math.sqrt(2) / 2, places=2)

        # Test case 9: Observer at equator, celestial body at 45 degrees south
        self.assertAlmostEqual(calculate_topocentric_distance(0, 0, 0, -45), 149.6e6 * math.sqrt(2) / 2, places=2)

if __name__ == '__main__':
    unittest.main()