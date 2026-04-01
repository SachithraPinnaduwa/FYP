import unittest

class TestTimeSeriesAggregator(unittest.TestCase):
    def setUp(self):
        self.aggregator = TimeSeriesAggregator()

    def test_add_point(self):
        self.aggregator.add_point(datetime(2023, 1, 1, 12, 0), 10.0)
        self.assertEqual(len(self.aggregator.data), 1)
        self.assertEqual(self.aggregator.data[0]["val"], 10.0)

    def test_aggregate_by_day_single_point(self):
        self.aggregator.add_point(datetime(2023, 1, 1, 12, 0), 10.0)
        results = self.aggregator.aggregate_by_day()
        self.assertEqual(len(results), 1)
        self.assertEqual(results["2023-01-01"]["sum"], 10.0)
        self.assertEqual(results["2023-01-01"]["count"], 1)
        self.assertEqual(results["2023-01-01"]["avg"], 10.0)

    def test_aggregate_by_day_multiple_points_same_day(self):
        self.aggregator.add_point(datetime(2023, 1, 1, 12, 0), 10.0)
        self.aggregator.add_point(datetime(2023, 1, 1, 13, 0), 20.0)
        results = self.aggregator.aggregate_by_day()
        self.assertEqual(len(results), 1)
        self.assertEqual(results["2023-01-01"]["sum"], 30.0)
        self.assertEqual(results["2023-01-01"]["count"], 2)
        self.assertEqual(results["2023-01-01"]["avg"], 15.0)
        self.assertEqual(results["2023-01-01"]["min"], 10.0)
        self.assertEqual(results["2023-01-01"]["max"], 20.0)

    def test_aggregate_by_day_multiple_days(self):
        self.aggregator.add_point(datetime(2023, 1, 1, 12, 0), 10.0)
        self.aggregator.add_point(datetime(2023, 1, 2, 12, 0), 20.0)
        results = self.aggregator.aggregate_by_day()
        self.assertEqual(len(results), 2)
        self.assertEqual(results["2023-01-01"]["sum"], 10.0)
        self.assertEqual(results["2023-01-01"]["count"], 1)
        self.assertEqual(results["2023-01-01"]["avg"], 10.0)
        self.assertEqual(results["2023-01-02"]["sum"], 20.0)
        self.assertEqual(results["2023-01-02"]["count"], 1)
        self.assertEqual(results["2023-01-02"]["avg"], 20.0)

    def test_aggregate_by_day_with_zero_value(self):
        self.aggregator.add_point(datetime(2023, 1, 1, 12, 0), 0.0)
        results = self.aggregator.aggregate_by_day()
        self.assertEqual(len(results), 1)
        self.assertEqual(results["2023-01-01"]["sum"], 0.0)
        self.assertEqual(results["2023-01-01"]["count"], 1)
        self.assertEqual(results["2023-01-01"]["avg"], 0.0)

    def test_aggregate_by_day_with_negative_value(self):
        self.aggregator.add_point(datetime(2023, 1, 1, 12, 0), -10.0)
        results = self.aggregator.aggregate_by_day()
        self.assertEqual(len(results), 1)
        self.assertEqual(results["2023-01-01"]["sum"], -10.0)
        self.assertEqual(results["2023-01-01"]["count"], 1)
        self.assertEqual(results["2023-01-01"]["avg"], -10.0)

    def test_aggregate_by_day_with_large_values(self):
        self.aggregator.add_point(datetime(2023, 1, 1, 12, 0), 1000000.0)
        results = self.aggregator.aggregate_by_day()
        self.assertEqual(len(results), 1)
        self.assertEqual(results["2023-01-01"]["sum"], 1000000.0)
        self.assertEqual(results["2023-01-01"]["count"], 1)
        self.assertEqual(results["2023-01-01"]["avg"], 1000000.0)

    def test_aggregate_by_day_with_many_points(self):
        for i in range(100):
            self.aggregator.add_point(datetime(2023, 1, 1, 12, 0), i * 10.0)
        results = self.aggregator.aggregate_by_day()
        self.assertEqual(len(results), 1)
        self.assertEqual(results["2023-01-01"]["count"], 100)
        self.assertEqual(results["2023-01-01"]["sum"], 49500.0)
        self.assertEqual(results["2023-01-01"]["avg"], 495.0)

    def test_aggregate_by_day_with_empty_data(self):
        results = self.aggregator.aggregate_by_day()
        self.assertEqual(len(results), 0)

if __name__ == "__main__":
    unittest.main()
