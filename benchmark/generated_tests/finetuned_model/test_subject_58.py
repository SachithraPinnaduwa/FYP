import math
import unittest

class TestCalculateTopocentricDistance(unittest.TestCase):

    def test_zero_distance(self):
        # Test case when the observer and the celestial object are on the same meridian
        observer_lat = 0
        observer_lon = 0
        celestial_ra = 0
        celestial_dec = 0
        self.assertAlmostEqual(calculate_topocentric_distance(observer_lat, observer_lon, celestial_ra, celestial_dec), 149.6 * 10**6, places=2)

    def test_north_pole(self):
        # Test case when the observer is at the North Pole
        observer_lat = 90
        observer_lon = 0
        celestial_ra = 0
        celestial_dec = 0
        self.assertAlmostEqual(calculate_topocentric_distance(observer_lat, observer_lon, celestial_ra, celestial_dec), 149.6 * 10**6, places=2)

    def test_south_pole(self):
        # Test case when the observer is at the South Pole
        observer_lat = -90
        observer_lon = 0
        celestial_ra = 0
        celestial_dec = 0
        self.assertAlmostEqual(calculate_topocentric_distance(observer_lat, observer_lon, celestial_ra, celestial_dec), 149.6 * 10**6, places=2)

    def test_equator(self):
        # Test case when the observer is on the equator
        observer_lat = 0
        observer_lon = 0
        celestial_ra = 0
        celestial_dec = 90
        self.assertAlmostEqual(calculate_topocentric_distance(observer_lat, observer_lon, celestial_ra, celestial_dec), 149.6 * 10**6, places=2)

    def test_different_declination(self):
        # Test case with different declination
        observer_lat = 0
        observer_lon = 0
        celestial_ra = 0
        celestial_dec = 30
        self.assertAlmostEqual(calculate_topocentric_distance(observer_lat, observer_lon, celestial_ra, celestial_dec), 149.6 * 10**6 * math.acos(math.sin(math.radians(30)) * math.sin(math.radians(0)) + math.cos(math.radians(30)) * math.cos(math.radians(0)) * math.cos(math.radians(0))) / 6371, places=2)

    def test_different_longitude(self):
        # Test case with different longitude
        observer_lat = 0
        observer_lon = 30
        celestial_ra = 0
        celestial_dec = 0
        self.assertAlmostEqual(calculate_topocentric_distance(observer_lat, observer_lon, celestial_ra, celestial_dec), 149.6 * 10**6 * math.acos(math.sin(math.radians(0)) * math.sin(math.radians(0)) + math.cos(math.radians(0)) * math.cos(math.radians(0)) * math.cos(math.radians(-30))) / 6371, places=2)

    def test_different_latitude(self):
        # Test case with different latitude
        observer_lat = 30
        observer_lon = 0
        celestial_ra = 0
        celestial_dec = 0
        self.assertAlmostEqual(calculate_topocentric_distance(observer_lat, observer_lon, celestial_ra, celestial_dec), 149.6 * 10**6 * math.acos(math.sin(math.radians(30)) * math.sin(math.radians(30)) + math.cos(math.radians(30)) * math.cos(math.radians(30)) * math.cos(math.radians(0))) / 6371, places=2)

    def test_different_ra_and_dec(self):
        # Test case with different right ascension and declination
        observer_lat = 0
        observer_lon = 0
        celestial_ra = 12
        celestial_dec = 30
        self.assertAlmostEqual(calculate_topocentric_distance(observer_lat, observer_lon, celestial_ra, celestial_dec), 149.6 * 10**6 * math.acos(math.sin(math.radians(30)) * math.sin(math.radians(0)) + math.cos(math.radians(30)) * math.cos(math.radians(0)) * math.cos(math.radians(-12))) / 6371, places=2)