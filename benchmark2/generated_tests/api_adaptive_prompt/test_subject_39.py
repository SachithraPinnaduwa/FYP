from subject_39 import *

import unittest

def estimated_impact(beta0, beta1, beta2, std_err_beta2, p_value_beta2):
    """
    Calculate the estimated impact of education on wage for non-college and college graduates,
    and determine if the impacts are significantly different.

    Parameters:
    - beta0 (float): Intercept of the linear regression model
    - beta1 (float): Coefficient of educ in the linear regression model
    - beta2 (float): Coefficient of educ*college in the linear regression model
    - std_err_beta2 (float): Standard error of beta2
    - p_value_beta2 (float): P-value of beta2

    Returns:
    - impact_non_college (float): Estimated impact of educ on wage for non-college graduates
    - impact_college (float): Estimated impact of educ on wage for college graduates
    - is_impact_different (bool): Whether the impacts for the two groups are significantly different
    """

    # Estimated impact of educ on wage for non-college graduates
    impact_non_college = beta1

    # Estimated impact of educ on wage for college graduates
    impact_college = beta1 + beta2

    # Check if the impact is significantly different for the two groups
    # Assuming a significance level of 0.05
    is_impact_different = p_value_beta2 < 0.05

    return impact_non_college, impact_college, is_impact_different

class TestEstimatedImpact(unittest.TestCase):
    def test_normal_case(self):
        beta0 = 0.5
        beta1 = 0.2
        beta2 = 0.1
        std_err_beta2 = 0.05
        p_value_beta2 = 0.03
        expected_impact_non_college = 0.2
        expected_impact_college = 0.3
        expected_is_impact_different = True
        impact_non_college, impact_college, is_impact_different = estimated_impact(beta0, beta1, beta2, std_err_beta2, p_value_beta2)
        self.assertEqual(impact_non_college, expected_impact_non_college)
        self.assertEqual(impact_college, expected_impact_college)
        self.assertEqual(is_impact_different, expected_is_impact_different)

    def test_edge_case(self):
        beta0 = 0.5
        beta1 = 0.2
        beta2 = 0.1
        std_err_beta2 = 0.05
        p_value_beta2 = 0.05
        expected_impact_non_college = 0.2
        expected_impact_college = 0.3
        expected_is_impact_different = False
        impact_non_college, impact_college, is_impact_different = estimated_impact(beta0, beta1, beta2, std_err_beta2, p_value_beta2)
        self.assertEqual(impact_non_college, expected_impact_non_college)
        self.assertEqual(impact_college, expected_impact_college)
        self.assertEqual(is_impact_different, expected_is_impact_different)

    def test_error_handling(self):
        beta0 = -0.5
        beta1 = -0.2
        beta2 = -0.1
        std_err_beta2 = -0.05
        p_value_beta2 = 0.03
        with self.assertRaises(ValueError):
            estimated_impact(beta0, beta1, beta2, std_err_beta2, p_value_beta2)

if __name__ == '__main__':
    unittest.main()