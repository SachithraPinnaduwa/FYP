```python
import unittest

class TestCalculateProgressChecks(unittest.TestCase):
    def test_calculate_progress_checks(self):
        self.assertEqual(calculate_progress_checks(15000, 1000, 1000), 1)
        self.assertEqual(calculate_progress_checks(15000, 1000, 100), 15)
        self.assertEqual(calculate_progress_checks(15000, 1000, 10000), 0)
        self.assertEqual(calculate_progress_checks(15000, 1000, 100000), 0)
        self.assertEqual(calculate_progress_checks(15000, 1000, 1000000), 0)
        self.assertEqual(calculate_progress_checks(15000, 1000, 10000000), 0)
        self.assertEqual(calculate_progress_checks(15000, 1000, 100000000), 0)
        self.assertEqual(calculate_progress_checks(15000, 1000, 1000000000), 0)
        self.assertEqual(calculate_progress_checks(15000, 1000, 10000000000), 0)
        self.assertEqual(calculate_progress_checks(15000, 1000, 100000000000), 0)
        self.assertEqual(calculate_progress_checks(15000, 1000, 1000000000000), 0)
        self.assertEqual(calculate_progress_checks(15000, 1000, 10000000000000), 0)
        self.assertEqual(calculate_progress_checks(15000, 1000, 100000000000000), 0)