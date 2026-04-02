from subject_58 import *

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
    def test_calculate_topocentric_distance(self):
        self.assertAlmostEqual(calculate_topocentric_distance(34.0522, -118.2437, 12.2597, 27.8284), 149.6 * 10**6 * math.acos(math.sin(math.radians(27.8284)) * math.sin(math.radians(34.0522)) + math.cos(math.radians(27.8284)) * math.cos(math.radians(34.0522)) * math.cos(math.radians(-118.2437 - 12.2597))) / 6371, places=5)

if __name__ == '__main__':
    unittest.main()