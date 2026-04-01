import unittest

class TestFindKForDigitPowerSum(unittest.TestCase):
    
    def test_base_case(self):
        # Test with the base case from the problem description
        self.assertEqual(find_k_for_digit_power_sum(89, 1), 1)
    
    def test_no_k_exists(self):
        # Test with a case where no k exists
        self.assertEqual(find_k_for_digit_power_sum(92, 1), -1)
    
    def test_example_case(self):
        # Test with an example case from the problem description
        self.assertEqual(find_k_for_digit_power_sum(695, 2), 2)
    
    def test_large_number_case(self):
        # Test with a large number case from the problem description
        self.assertEqual(find_k_for_digit_power_sum(46288, 3), 51)
    
    def test_single_digit_case(self):
        # Test with a single digit case
        self.assertEqual(find_k_for_digit_power_sum(10, 1), -1)
    
    def test_zero_case(self):
        # Test with a zero case
        self.assertEqual(find_k_for_digit_power_sum(0, 1), -1)
    
    def test_large_p_case(self):
        # Test with a large p case
        self.assertEqual(find_k_for_digit_power_sum(100, 2), 100)