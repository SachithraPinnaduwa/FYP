import unittest

class TestGeoDistance(unittest.TestCase):
    def test_haversine(self):
        # Test case 1: Known distance between two points
        lat1, lon1 = 37.7749, -122.4194  # San Francisco
        lat2, lon2 = 34.0522, -118.2437  # Los Angeles
        expected_distance = 559.0  # Approximate distance in km
        self.assertAlmostEqual(GeoDistance.haversine(lat1, lon1, lat2, lon2), expected_distance, places=1)

        # Test case 2: Same location (distance should be 0)
        lat1, lon1 = 37.7749, -122.4194
        lat2, lon2 = 37.7749, -122.4194
        self.assertAlmostEqual(GeoDistance.haversine(lat1, lon1, lat2, lon2), 0, places=1)

        # Test case 3: Points at the same latitude but different longitude
        lat1, lon1 = 37.7749, -122.4194
        lat2, lon2 = 37.7749, -122.4194 + 10  # 10 degrees difference in longitude
        self.assertGreater(GeoDistance.haversine(lat1, lon1, lat2, lon2), 0)

    def test_bounding_box(self):
        # Test case 1: Bounding box for a specific distance
        lat, lon = 37.7749, -122.4194
        distance_km = 100.0
        bounding_box = GeoDistance.bounding_box(lat, lon, distance_km)
        self.assertIn("min_lat", bounding_box)
        self.assertIn("max_lat", bounding_box)
        self.assertIn("min_lon", bounding_box)
        self.assertIn("max_lon", bounding_box)

        # Test case 2: Bounding box for a larger distance
        lat, lon = 37.7749, -122.4194
        distance_km = 1000.0
        bounding_box = GeoDistance.bounding_box(lat, lon, distance_km)
        self.assertGreater(bounding_box["min_lat"], lat - 10)
        self.assertLess(bounding_box["max_lat"], lat + 10)
        self.assertGreater(bounding_box["min_lon"], lon - 10)
        self.assertLess(bounding_box["max_lon"], lon + 10)

if __name__ == '__main__':
    unittest.main()
