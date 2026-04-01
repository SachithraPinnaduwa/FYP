import unittest
from math import ceil

def calculate_progress_checks(match_time, time_step, progress_check_threshold):
    progress_check_steps = ceil(15 / (time_step / 1000.0))  
    total_checks = match_time / time_step  
    checks_per_progress_check = ceil(total_checks / progress_check_steps)  
    progress_checks = ceil(total_checks / checks_per_progress_check)  
    return progress_checks

class TestCalculateProgressChecks(unittest.TestCase):

    def test_calculate_progress_checks(self):
        # Test case with typical values
        self.assertEqual(calculate_progress_checks(90000, 3000, 0.2), 1)
        
        # Test case with small match time
        self.assertEqual(calculate_progress_checks(1000, 1000, 0.2), 1)
        
        # Test case with large match time
        self.assertEqual(calculate_progress_checks(3600000, 60000, 0.2), 1)
        
        # Test case with very small time step
        self.assertEqual(calculate_progress_checks(180000, 100, 0.2), 1)
        
        # Test case with zero match time
        self.assertEqual(calculate_progress_checks(0, 3000, 0.2), 0)
        
        # Test case with negative match time
        with self.assertRaises(ValueError):
            calculate_progress_checks(-180000, 3000, 0.2)
        
        # Test case with zero time step
        with self.assertRaises(ValueError):
            calculate_progress_checks(180000, 0, 0.2)
        
        # Test case with negative time step
        with self.assertRaises(ValueError):
            calculate_progress_checks(180000, -3000, 0.2)

if __name__ == '__main__':
    unittest.main()