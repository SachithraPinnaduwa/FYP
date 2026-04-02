import unittest

class TestEstimatedImpact(unittest.TestCase):
    def test_estimated_impact(self):
        # Test case 1: Typical scenario with positive beta2
        beta0 = 2.5
        beta1 = 0.3
        beta2 = 0.1
        std_err_beta2 = 0.05
        p_value_beta2 = 0.03
        expected_impact_non_college = 0.3
        expected_impact_college = 0.4
        expected_is_impact_different = True
        actual_impact_non_college, actual_impact_college, actual_is_impact_different = estimated_impact(beta0, beta1, beta2, std_err_beta2, p_value_beta2)
        self.assertAlmostEqual(actual_impact_non_college, expected_impact_non_college, places=4)
        self.assertAlmostEqual(actual_impact_college, expected_impact_college, places=4)
        self.assertEqual(actual_is_impact_different, expected_is_impact_different)

        # Test case 2: Scenario with beta2 = 0 (no impact of college education)
        beta2 = 0
        expected_impact_college = 0.3
        expected_is_impact_different = False
        actual_impact_non_college, actual_impact_college, actual_is_impact_different = estimated_impact(beta0, beta1, beta2, std_err_beta2, p_value_beta2)
        self.assertAlmostEqual(actual_impact_non_college, expected_impact_non_college, places=4)
        self.assertAlmostEqual(actual_impact_college, expected_impact_college, places=4)
        self.assertEqual(actual_is_impact_different, expected_is_impact_different)

        # Test case 3: Scenario with a very high p-value for beta2 (no significant difference)
        p_value_beta2 = 0.1
        expected_is_impact_different = False
        actual_impact_non_college, actual_impact_college, actual_is_impact_different = estimated_impact(beta0, beta1, beta2, std_err_beta2, p_value_beta2)
        self.assertEqual(actual_is_impact_different, expected_is_impact_different)

        # Test case 4: Scenario with a negative beta2 (negative impact of college education)
        beta2 = -0.1
        expected_impact_college = 0.2
        expected_is_impact_different = True
        actual_impact_non_college, actual_impact_college, actual_is_impact_different = estimated_impact(beta0, beta1, beta2, std_err_beta2, p_value_beta2)
        self.assertAlmostEqual(actual_impact_non_college, expected_impact_non_college, places=4)
        self.assertAlmostEqual(actual_impact_college, expected_impact_college, places=4)
        self.assertEqual(actual_is_impact_different, expected_is_impact_different)

if __name__ == '__main__':
    unittest.main()