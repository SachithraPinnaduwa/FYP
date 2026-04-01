import unittest

class TestEstimatedImpact(unittest.TestCase):

    def test_estimated_impact(self):
        # Test case 1: Impact calculation for non-college and college graduates
        beta0 = 2.5
        beta1 = 0.8
        beta2 = 0.4
        std_err_beta2 = 0.2
        p_value_beta2 = 0.03
        
        expected_impact_non_college = beta1
        expected_impact_college = beta1 + beta2
        expected_is_impact_different = True
        
        result = estimated_impact(beta0, beta1, beta2, std_err_beta2, p_value_beta2)
        
        self.assertEqual(result[0], expected_impact_non_college)
        self.assertEqual(result[1], expected_impact_college)
        self.assertEqual(result[2], expected_is_impact_different)

    def test_estimated_impact_no_difference(self):
        # Test case 2: Impact calculation when there is no significant difference
        beta0 = 2.5
        beta1 = 0.8
        beta2 = 0.4
        std_err_beta2 = 0.2
        p_value_beta2 = 0.1
        
        expected_impact_non_college = beta1
        expected_impact_college = beta1 + beta2
        expected_is_impact_different = False
        
        result = estimated_impact(beta0, beta1, beta2, std_err_beta2, p_value_beta2)
        
        self.assertEqual(result[0], expected_impact_non_college)
        self.assertEqual(result[1], expected_impact_college)
        self.assertEqual(result[2], expected_is_impact_different)

    def test_estimated_impact_negative_beta2(self):
        # Test case 3: Impact calculation with negative beta2
        beta0 = 2.5
        beta1 = 0.8
        beta2 = -0.4
        std_err_beta2 = 0.2
        p_value_beta2 = 0.03
        
        expected_impact_non_college = beta1
        expected_impact_college = beta1 + beta2
        expected_is_impact_different = True
        
        result = estimated_impact(beta0, beta1, beta2, std_err_beta2, p_value_beta2)
        
        self.assertEqual(result[0], expected_impact_non_college)
        self.assertEqual(result[1], expected_impact_college)
        self.assertEqual(result[2], expected_is_impact_different)

if __name__ == '__main__':
    unittest.main()