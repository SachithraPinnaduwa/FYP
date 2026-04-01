import unittest

class TestEstimatedImpactFunction(unittest.TestCase):

    def test_base_case(self):
        # Test with base values and check if the function returns the correct results
        beta0 = 0.5
        beta1 = 0.3
        beta2 = 0.2
        std_err_beta2 = 0.1
        p_value_beta2 = 0.03
        expected_impact_non_college = beta1
        expected_impact_college = beta1 + beta2
        expected_is_impact_different = True

        self.assertAlmostEqual(estimated_impact(beta0, beta1, beta2, std_err_beta2, p_value_beta2)[0], expected_impact_non_college, places=3)
        self.assertAlmostEqual(estimated_impact(beta0, beta1, beta2, std_err_beta2, p_value_beta2)[1], expected_impact_college, places=3)
        self.assertEqual(estimated_impact(beta0, beta1, beta2, std_err_beta2, p_value_beta2)[2], expected_is_impact_different)

    def test_zero_impact_non_college(self):
        # Test with a zero impact for non-college graduates
        beta0 = 0.5
        beta1 = 0.0
        beta2 = 0.2
        std_err_beta2 = 0.1
        p_value_beta2 = 0.05
        expected_impact_non_college = beta1
        expected_impact_college = beta1 + beta2
        expected_is_impact_different = False

        self.assertAlmostEqual(estimated_impact(beta0, beta1, beta2, std_err_beta2, p_value_beta2)[0], expected_impact_non_college, places=3)
        self.assertAlmostEqual(estimated_impact(beta0, beta1, beta2, std_err_beta2, p_value_beta2)[1], expected_impact_college, places=3)
        self.assertEqual(estimated_impact(beta0, beta1, beta2, std_err_beta2, p_value_beta2)[2], expected_is_impact_different)

    def test_zero_impact_college(self):
        # Test with a zero impact for college graduates
        beta0 = 0.5
        beta1 = 0.3
        beta2 = 0.0
        std_err_beta2 = 0.1
        p_value_beta2 = 0.05
        expected_impact_non_college = beta1
        expected_impact_college = beta1 + beta2
        expected_is_impact_different = False

        self.assertAlmostEqual(estimated_impact(beta0, beta1, beta2, std_err_beta2, p_value_beta2)[0], expected_impact_non_college, places=3)
        self.assertAlmostEqual(estimated_impact(beta0, beta1, beta2, std_err_beta2, p_value_beta2)[1], expected_impact_college, places=3)
        self.assertEqual(estimated_impact(beta0, beta1, beta2, std_err_beta2, p_value_beta2)[2], expected_is_impact_different)

    def test_large_p_value(self):
        # Test with a large p-value indicating no significant difference
        beta0 = 0.5
        beta1 = 0.3
        beta2 = 0.2
        std_err_beta2 = 0.1
        p_value_beta2 = 0.1
        expected_impact_non_college = beta1
        expected_impact_college = beta1 + beta2
        expected_is_impact_different = False

        self.assertAlmostEqual(estimated_impact(beta0, beta1, beta2, std_err_beta2, p_value_beta2)[0], expected_impact_non_college, places=3)
        self.assertAlmostEqual(estimated_impact(beta0, beta1, beta2, std_err_beta2, p_value_beta2)[1], expected_impact_college, places=3)
        self.assertEqual(estimated_impact(beta0, beta1, beta2, std_err_beta2, p_value_beta2)[2], expected_is_impact_different)