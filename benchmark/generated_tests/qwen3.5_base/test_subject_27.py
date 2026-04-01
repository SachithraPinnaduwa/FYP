import unittest

class TestMetricsRegistry(unittest.TestCase):
    def setUp(self):
        self.registry = MetricsRegistry()

    def test_inc_counter(self):
        self.registry.inc_counter("test_counter", 5)
        self.assertEqual(self.registry.counters["test_counter"], 5)

    def test_inc_counter_multiple(self):
        self.registry.inc_counter("test_counter", 3)
        self.registry.inc_counter("test_counter", 2)
        self.assertEqual(self.registry.counters["test_counter"], 5)

    def test_set_gauge(self):
        self.registry.set_gauge("test_gauge", 10.5)
        self.assertEqual(self.registry.gauges["test_gauge"], 10.5)

    def test_report(self):
        self.registry.inc_counter("counter1", 1)
        self.registry.inc_counter("counter2", 2)
        self.registry.set_gauge("gauge1", 1.5)
        self.registry.set_gauge("gauge2", 2.5)
        report = self.registry.report()
        self.assertEqual(report["counters"]["counter1"], 1)
        self.assertEqual(report["counters"]["counter2"], 2)
        self.assertEqual(report["gauges"]["gauge1"], 1.5)
        self.assertEqual(report["gauges"]["gauge2"], 2.5)

if __name__ == "__main__":
    unittest.main()
