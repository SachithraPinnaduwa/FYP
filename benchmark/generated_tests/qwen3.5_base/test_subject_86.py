import unittest

class TestGeoHash(unittest.TestCase):
    def test_encode_decode(self):
        lat, lon = 40.7128, -74.0060
        geohash = GeoHash.encode(lat, lon, precision=12)
        decoded_lat, decoded_lon = GeoHash.decode(geohash)
        self.assertAlmostEqual(lat, decoded_lat, places=6)
        self.assertAlmostEqual(lon, decoded_lon, places=6)

    def test_encode_decode_precision(self):
        lat, lon = 40.7128, -74.0060
        for precision in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
            geohash = GeoHash.encode(lat, lon, precision=precision)
            decoded_lat, decoded_lon = GeoHash.decode(geohash)
            self.assertAlmostEqual(lat, decoded_lat, places=precision)
            self.assertAlmostEqual(lon, decoded_lon, places=precision)

    def test_encode_decode_boundary(self):
        lat, lon = -90.0, -180.0
        geohash = GeoHash.encode(lat, lon, precision=12)
        decoded_lat, decoded_lon = GeoHash.decode(geohash)
        self.assertAlmostEqual(lat, decoded_lat, places=6)
        self.assertAlmostEqual(lon, decoded_lon, places=6)

    def test_encode_decode_boundary_positive(self):
        lat, lon = 90.0, 180.0
        geohash = GeoHash.encode(lat, lon, precision=12)
        decoded_lat, decoded_lon = GeoHash.decode(geohash)
        self.assertAlmostEqual(lat, decoded_lon, places=6)
        self.assertAlmostEqual(lon, decoded_lon, places=6)

    def test_encode_decode_boundary_negative(self):
        lat, lon = -90.0, 180.0
        geohash = GeoHash.encode(lat, lon, precision=12)
        decoded_lat, decoded_lon = GeoHash.decode(geohash)
        self.assertAlmostEqual(lat, decoded_lon, places=6)
        self.assertAlmostEqual(lon, decoded_lon, places=6)

    def test_encode_decode_boundary_negative(self):
        lat, lon = -90.0, -180.0
        geohash = GeoHash.encode(lat, lon, precision=12)
        decoded_lat, decoded_lon = GeoHash.decode(geohash)
        self.assertAlmostEqual(lat, decoded_lon, places=6)
        self.assertAlmostEqual(lon, decoded_lon, places=6)

    def test_encode_decode_boundary_negative(self):
        lat, lon = -90.0, -180.0
        geohash = GeoHash.encode(lat, lon, precision=12)
        decoded_lat, decoded_lon = GeoHash.decode(geohash)
        self.assertAlmostEqual(lat, decoded_lon, places=6)
        self.assertAlmostEqual(lon, decoded_lon, places=6)

    def test_encode_decode_boundary_negative(self):
        lat, lon = -90.0, -180.0
        geohash = GeoHash.encode(lat, lon, precision=12)
        decoded_lat, decoded_lon = GeoHash.decode(geohash)
        self.assertAlmostEqual(lat, decoded_lon, places=6)
        self.assertAlmostEqual(lon, decoded_lon, places=6)

    def test_encode_decode_boundary_negative(self):
        lat, lon = -90.0, -180.0
        geohash = GeoHash.encode(lat, lon, precision=12)
        decoded_lat, decoded_lon = GeoHash.decode(geohash)
        self.assertAlmostEqual(lat, decoded_lon, places=6)
        self.assertAlmostEqual(lon, decoded_lon, places=6)

    def test_encode_decode_boundary_negative(self):
        lat, lon = -90.0, -180.0
        geohash = GeoHash.encode(lat, lon, precision=12)
        decoded_lat, decoded_lon = GeoHash.decode(geohash)
        self.assertAlmostEqual(lat, decoded_lon, places=6)
        self.assertAlmostEqual(lon, decoded_lon, places=6)

    def test_encode_decode_boundary_negative(self):
        lat, lon = -90.0, -180.0
        geohash = GeoHash.encode(lat, lon, precision=12)
        decoded_lat, decoded_lon = GeoHash.decode(geohash)
        self.assertAlmostEqual(lat, decoded_lon, places=6)
        self.assertAlmostEqual(lon, decoded_lon, places=6)

    def test_encode_decode_boundary_negative(self):
        lat, lon = -90.0, -180.0
        geohash = GeoHash.encode(lat, lon, precision=12)
        decoded_lat, decoded_lon = GeoHash.decode(geohash)
        self.assertAlmostEqual(lat, decoded_lon, places=6)
        self.assertAlmostEqual(lon, decoded_lon, places=6)

    def test_encode_decode_boundary_negative(self):
        lat, lon = -90.0, -180.0
        geohash = GeoHash.encode(lat, lon, precision=12)
        decoded_lat, decoded_lon = GeoHash.decode(geohash)
        self.assertAlmostEqual(lat, decoded_lon, places=6)
        self.assertAlmostEqual(lon, decoded_lon, places=6)

    def test_encode_decode_boundary_negative(self):
        lat, lon = -90.0, -180.0
        geohash = GeoHash.encode(lat, lon, precision=12)
        decoded_lat, decoded_lon = GeoHash.decode(geohash)
        self.assertAlmostEqual(lat, decoded_lon, places=6)
        self.assertAlmostEqual(lon, decoded_lon, places=6)

    def test_encode_decode_boundary_negative(self):
        lat, lon = -90.0, -180.0
        geohash = GeoHash.encode(lat, lon, precision=12)
        decoded_lat, decoded_lon = GeoHash.decode(geohash)
        self.assertAlmostEqual(lat, decoded_lon, places=6)
        self.assertAlmostEqual(lon, decoded_lon, places=6)

    def test_encode_decode_boundary_negative(self):
        lat, lon = -90.0, -180.0
        geohash = GeoHash.encode(lat, lon, precision=12)
        decoded_lat, decoded_lon = GeoHash.decode(geohash)
        self.assertAlmostEqual(lat, decoded_lon, places=6)
        self.assertAlmostEqual(lon, decoded_lon, places=6)

    def test_encode_decode_boundary_negative(self):
        lat, lon = -90.0, -180.0
        geohash = GeoHash.encode(lat, lon, precision=12)
        decoded_lat, decoded_lon = GeoHash.decode(geohash)
        self.assertAlmostEqual(lat, decoded_lon, places