from subject_96 import *

import unittest

def calculate_progress_checks(match_time, time_step, progress_check_threshold):
    progress_check_steps = ceil(15 / (time_step / 1000.0))  
    total_checks = match_time / time_step  
    checks_per_progress_check = ceil(total_checks / progress_check_steps)  
    progress_checks = ceil(total_checks / checks_per_progress_check)  
    return progress_checks

class TestCalculateProgressChecks(unittest.TestCase):
    def test_calculate_progress_checks(self):
        self.assertEqual(calculate_progress_checks(10000, 1000, 0.1), 1)
        self.assertEqual(calculate_progress_checks(10000, 500, 0.1), 2)
        self.assertEqual(calculate_progress_checks(10000, 1000, 0.5), 1)
        self.assertEqual(calculate_progress_checks(10000, 500, 0.5), 2)
        self.assertEqual(calculate_progress_checks(10000, 1000, 1.0), 1)
        self.assertEqual(calculate_progress_checks(10000, 500, 1.0), 2)
        self.assertEqual(calculate_progress_checks(10000, 1000, 2.0), 1)
        self.assertEqual(calculate_progress_checks(10000, 500, 2.0), 2)
        self.assertEqual(calculate_progress_checks(10000, 1000, 5.0), 1)
        self.assertEqual(calculate_progress_checks(10000, 500, 5.0), 2)
        self.assertEqual(calculate_progress_checks(10000, 1000, 10.0), 1)
        self.assertEqual(calculate_progress_checks(10000, 500, 10.0), 2)
        self.assertEqual(calculate_progress_checks(10000, 1000, 20.0), 1)
        self.assertEqual(calculate_progress_checks(10000, 500, 20.0), 2)
        self.assertEqual(calculate_progress_checks(10000, 1000, 50.0), 1)
        self.assertEqual(calculate_progress_checks(10000, 500, 50.0), 2)
        self.assertEqual(calculate_progress_checks(10000, 1000, 100.0), 1)
        self.assertEqual(calculate_progress_checks(10000, 500, 100.0), 2)
        self.assertEqual(calculate_progress_checks(10000, 1000, 200.0), 1)
        self.assertEqual(calculate_progress_checks(10000, 500, 200.0), 2)
        self.assertEqual(calculate_progress_checks(10000, 1000, 500.0), 1)
        self.assertEqual(calculate_progress_checks(10000, 500, 500.0), 2)
        self.assertEqual(calculate_progress_checks(10000, 1000, 1000.0), 1)
        self.assertEqual(calculate_progress_checks(10000, 500, 1000.0), 2)
        self.assertEqual(calculate_progress_checks(10000, 1000, 2000.0), 1)
        self.assertEqual(calculate_progress_checks(10000, 500, 2000.0), 2)
        self.assertEqual(calculate_progress_checks(10000, 1000, 5000.0), 1)
        self.assertEqual(calculate_progress_checks(10000, 500, 5000.0), 2)
        self.assertEqual(calculate_progress_checks(10000, 1000, 10000.0), 1)
        self.assertEqual(calculate_progress_checks(10000, 500, 10000.0), 2)

if __name__ == '__main__':
    unittest.main()