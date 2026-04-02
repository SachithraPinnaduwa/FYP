from subject_96 import *

import unittest

def calculate_progress_checks(match_time, time_step, progress_check_threshold):
    progress_check_steps = ceil(15 / (time_step / 1000.0))  
    total_checks = match_time / time_step  
    checks_per_progress_check = ceil(total_checks / progress_check_steps)  
    progress_checks = ceil(total_checks / checks_per_progress_check)  
    return progress_checks

class TestCalculateProgressChecks(unittest.TestCase):
    def test_normal_case(self):
        match_time = 120000
        time_step = 1000
        progress_check_threshold = 0.5
        expected = 12
        self.assertEqual(calculate_progress_checks(match_time, time_step, progress_check_threshold), expected)

    def test_edge_case(self):
        match_time = 1000
        time_step = 1
        progress_check_threshold = 0.0
        expected = 1
        self.assertEqual(calculate_progress_checks(match_time, time_step, progress_check_threshold), expected)

    def test_error_handling_negative_values(self):
        match_time = -1000
        time_step = -1
        progress_check_threshold = -0.5
        with self.assertRaises(ValueError):
            calculate_progress_checks(match_time, time_step, progress_check_threshold)

    def test_error_handling_zero_values(self):
        match_time = 0
        time_step = 0
        progress_check_threshold = 0.0
        with self.assertRaises(ValueError):
            calculate_progress_checks(match_time, time_step, progress_check_threshold)

if __name__ == '__main__':
    unittest.main()