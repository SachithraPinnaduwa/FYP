import unittest

class TestTopocentricDistance(unittest.TestCase):
    def test_basic_calculation(self):
        # Test case: observer at 0,0, celestial object at 0,0
        distance = calculate_topocentric_distance(0, 0, 0, 0)
        self.assertAlmostEqual(distance, 0, places=5)

    def test_observer_at_equator(self):
        # Test case: observer at equator, celestial object at 0,0
        distance = calculate_topocentric_distance(0, 0, 0, 0)
        self.assertAlmostEqual(distance, 0, places=5)

    def test_observer_at_pole(self):
        # Test case: observer at North Pole, celestial object at 0,0
        distance = calculate_topocentric_distance(90, 0, 0, 0)
        self.assertAlmostEqual(distance, 149.6 * 10**6 / 6371, places=5)

    def test_observer_at_different_lat_lon(self):
        # Test case: observer at 45, 45, celestial object at 0,0
        distance = calculate_topocentric_distance(45, 45, 0, 0)
        self.assertGreater(distance, 0)

    def test_celestial_object_at_different_ra_dec(self):
        # Test case: observer at 0,0, celestial object at 90, 90
        distance = calculate_topocentric_distance(0, 0, 90, 90)
        self.assertGreater(distance, 0)

if __name__ == '__main__':
    unittest.main()
