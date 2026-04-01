import unittest

class TestWeatherAPIClient(unittest.TestCase):
    def setUp(self):
        self.client = WeatherAPIClient(api_key="YOUR_API_KEY")

    def test_fetch_weather_success(self):
        result = self.client.fetch_weather("London")
        self.assertIsNotNone(result)
        self.assertIn("city", result)
        self.assertIn("temperature", result)
        self.assertIn("humidity", result)
        self.assertIn("conditions", result)

    def test_fetch_weather_cache(self):
        self.client.fetch_weather("London")
        self.client.fetch_weather("London")
        self.assertEqual(len(self.client.cache), 1)

    def test_fetch_weather_error_handling(self):
        result = self.client.fetch_weather("NonExistentCity")
        self.assertIsNone(result)

    def test_fetch_weather_units(self):
        result = self.client.fetch_weather("London", temp_unit="imperial")
        self.assertIsNotNone(result)

if __name__ == "__main__":
    unittest.main()
