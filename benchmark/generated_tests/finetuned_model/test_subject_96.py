import unittest

class TestCalculateProgressChecks(unittest.TestCase):

    def test_calculate_progress_checks_with_default_values(self):
        # Test with default values
        match_time = 10000  # 10 seconds
        time_step = 1000  # 1 second
        progress_check_threshold = 0.1  # 10%
        expected_output = 1
        self.assertEqual(calculate_progress_checks(match_time, time_step, progress_check_threshold), expected_output)

    def test_calculate_progress_checks_with_large_match_time(self):
        # Test with a larger match time
        match_time = 30000  # 30 seconds
        time_step = 500  # 500 milliseconds
        progress_check_threshold = 0.2  # 20%
        expected_output = 3
        self.assertEqual(calculate_progress_checks(match_time, time_step, progress_check_threshold), expected_output)

    def test_calculate_progress_checks_with_small_match_time(self):
        # Test with a smaller match time
        match_time = 5000  # 5 seconds
        time_step = 1000  # 1 second
        progress_check_threshold = 0.5  # 50%
        expected_output = 1
        self.assertEqual(calculate_progress_checks(match_time, time_step, progress_check_threshold), expected_output)

    def test_calculate_progress_checks_with_small_time_step(self):
        # Test with a small time step
        match_time = 10000  # 10 seconds
        time_step = 500  # 500 milliseconds
        progress_check_threshold = 0.1  # 10%
        expected_output = 2
        self.assertEqual(calculate_progress_checks(match_time, time_step, progress_check_threshold), expected_output)

    def test_calculate_progress_checks_with_large_progress_check_threshold(self):
        # Test with a large progress check threshold
        match_time = 10000  # 10 seconds
        time_step = 1000  # 1 second
        progress_check_threshold = 0.5  # 50%
        expected_output = 1
        self.assertEqual(calculate_progress_checks(match_time, time_step, progress_check_threshold), expected_output)

    def test_calculate_progress_checks_with_zero_match_time(self):
        # Test with zero match time
        match_time = 0  # 0 seconds
        time_step = 1000  # 1 second
        progress_check_threshold = 0.1  # 10%
        expected_output = 0
        self.assertEqual(calculate_progress_checks(match_time, time_step, progress_check_threshold), expected_output)

    def test_calculate_progress_checks_with_zero_time_step(self):
        # Test with zero time step (should raise an error)
        match_time = 10000  # 10 seconds
        time_step = 0  # 0 milliseconds
        progress_check_threshold = 0.1  # 10%
        with self.assertRaises(ZeroDivisionError):
            calculate_progress_checks(match_time, time_step, progress_check_threshold)