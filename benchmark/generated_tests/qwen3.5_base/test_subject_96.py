import unittest

class TestCalculateProgressChecks(unittest.TestCase):
    def test_progress_checks_calculation(self):
        match_time = 120  # minutes
        time_step = 1000  # milliseconds
        progress_check_threshold = 15  # percentage
        
        expected_progress_checks = 12
        actual_progress_checks = calculate_progress_checks(match_time, time_step, progress_check_threshold)
        
        self.assertEqual(actual_progress_checks, expected_progress_checks)

if __name__ == '__main__':
    unittest.main()
