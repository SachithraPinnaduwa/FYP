from subject_58 import *

```python
import unittest
import math

def calculate_topocentric_distance(observer_lat, observer_lon, celestial_ra, celestial_dec):
    observer_lat_rad = math.radians(observer_lat)
    celestial_dec_rad = math.radians(celestial_dec)
    celestial_ra_rad = math.radians(celestial_ra)
    observer_lon_rad = math.radians(observer_lon)

    phi = observer_lat_rad
    delta = celestial_dec_rad
    H = observer_lon_rad - celestial_ra_rad

    cos_d = math.sin(delta) * math.sin(phi) + math.cos(delta) * math.cos(phi) * math.cos(H)
    topocentric_distance = 149.6 * 10**6 * math.acos(cos_d) / 6371

    return topocentric_distance

class TestCalculateTopocentricDistance(unittest.TestCase):
    def test_normal_case_northern_hemisphere(self):
        observer_lat = 45
        observer_lon = 120
        celestial_ra = 12
        celestial_dec = 30
        expected = 149.6 * 10**6 * math.acos(math.sin(math.radians(30)) * math.sin(math.radians(45)) + math.cos(math.radians(30)) * math.cos(math.radians(45)) * math.cos(math.radians(120 - 12))) / 6371
        self.assertAlmostEqual(calculate_topocentric_distance(observer_lat, observer_lon, celestial_ra, celestial_dec), expected, places=2)

    def test_normal_case_southern_hemisphere(self):
        observer_lat = -45
        observer_lon = 120
        celestial_ra = 12
        celestial_dec = -30
        expected = 149.6 * 10**6 * math.acos(math.sin(math.radians(-30)) * math.sin(math.radians(-45)) + math.cos(math.radians(-30)) * math.cos(math.radians(-45)) * math.cos(math.radians(120 - 12))) / 6371
        self.assertAlmostEqual(calculate_topocentric_distance(observer_lat, observer_lon, celestial_ra, celestial_dec), expected, places=2)

    def test_normal_case_eastern_hemisphere(self):
        observer_lat = 45
        observer_lon = 180
        celestial_ra = 6
        celestial_dec = 0
        expected = 149.6 * 10**6 * math.acos(math.sin(math.radians(0)) * math.sin(math.radians(45)) + math.cos(math.radians(0)) * math.cos(math.radians(45)) * math.cos(math.radians(180 - 6))) / 6371
        self.assertAlmostEqual(calculate_topocentric_distance(observer_lat, observer_lon, celestial_ra, celestial_dec), expected, places=2)

    def test_normal_case_western_hemisphere(self):
        observer_lat = 45
        observer_lon = 0
        celestial_ra = 18
        celestial_dec = 0
        expected = 149.6 * 10**6 * math.acos(math.sin(math.radians(0)) * math.sin(math.radians(45)) + math.cos(math.radians(0)) * math.cos(math.radians(45)) * math.cos(math.radians(0 - 18))) / 6371
        self.assertAlmostEqual(calculate_topocentric_distance(observer_lat, observer_lon, celestial_ra, celestial_dec), expected, places=2)

    def test_edge_case_directly_overhead(self):
        observer_lat = 0
        observer_lon = 0
        celestial_ra = 0
        celestial_dec = 90
        expected = 149.6 * 10**6 * math.acos(math.sin(math.radians(90)) * math.sin(math.radians(0)) + math.cos(math.radians(90)) * math.cos(math.radians(0)) * math.cos(math.radians(0 - 0))) / 6371
        self.assertAlmostEqual(calculate_topocentric_distance(observer_lat, observer_lon, celestial_ra, celestial_dec), expected, places=2)

    def test_edge_case_directly_below(self):
        observer_lat = 0
        observer_lon = 0
        celestial_ra = 0
        celestial_dec = -90
        expected = 149.6 * 10**6 * math.acos(math.sin(math.radians(-90)) * math.sin(math.radians(0)) + math.cos(math.radians(-90)) * math.cos(math.radians(0)) * math.cos(math.radians(0 - 0))) / 6371
        self.assertAlmostEqual(calculate_topocentric_distance(observer_lat, observer_lon, celestial_ra, celestial_dec), expected, places=