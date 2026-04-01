import unittest

class TestSystemHealthChecker(unittest.TestCase):
    def setUp(self):
        self.checker = SystemHealthChecker()

    def test_record_metrics(self):
        self.checker.record_metrics(50.0, 60.0, 70.0)
        self.assertEqual(len(self.checker.records), 1)
        self.assertEqual(self.checker.records[0]["status"], "HEALTHY")

    def test_record_metrics_warning(self):
        self.checker.record_metrics(85.0, 60.0, 70.0)
        self.assertEqual(len(self.checker.records), 1)
        self.assertEqual(self.checker.records[0]["status"], "WARNING")

    def test_record_metrics_critical(self):
        self.checker.record_metrics(95.0, 60.0, 70.0)
        self.assertEqual(len(self.checker.records), 1)
        self.assertEqual(self.checker.records[0]["status"], "CRITICAL")

    def test_get_latest_status(self):
        self.checker.record_metrics(50.0, 60.0, 70.0)
        self.checker.record_metrics(85.0, 60.0, 70.0)
        self.checker.record_metrics(95.0, 60.0, 70.0)
        self.assertEqual(self.checker.get_latest_status(), "CRITICAL")

    def test_alert_needed(self):
        self.checker.record_metrics(50.0, 60.0, 70.0)
        self.checker.record_metrics(85.0, 60.0, 70.0)
        self.checker.record_metrics(95.0, 60.0, 70.0)
        self.assertFalse(self.checker.alert_needed())
        self.checker.record_metrics(95.0, 60.0, 70.0)
        self.assertTrue(self.checker.alert_needed())

if __name__ == "__main__":
    unittest.main()
