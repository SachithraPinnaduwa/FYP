import unittest

class TestEstimatedImpact(unittest.TestCase):
    def test_impact_non_college(self):
        """Test the estimated impact of educ on wage for non-college graduates"""
        beta0 = 10.0
        beta1 = 2.0
        beta2 = 0.5
        std_err_beta2 = 0.1
        p_value_beta2 = 0.01

        impact_non_college, impact_college, is_impact_different = estimated_impact(beta0, beta1, beta2, std_err_beta2, p_value_beta2)

        self.assertEqual(impact_non_college, 2.0)

    def test_impact_college(self):
        """Test the estimated impact of educ on wage for college graduates"""
        beta0 = 10.0
        beta1 = 2.0
        beta2 = 0.5
        std_err_beta2 = 0.1
        p_value_beta2 = 0.01

        impact_non_college, impact_college, is_impact_different = estimated_impact(beta0, beta1, beta2, std_err_beta2, p_value_beta2)

        self.assertEqual(impact_college, 2.5)

    def test_is_impact_different(self):
        """Test if the impacts for the two groups are significantly different"""
        beta0 = 10.0
        beta1 = 2.0
        beta2 = 0.5
        std_err_beta2 = 0.1
        p_value_beta2 = 0.01

        impact_non_college, impact_college, is_impact_different = estimated_impact(beta0, beta1, beta2, std_err_beta2, p_value_beta2)

        self.assertTrue(is_impact_different)

    def test_impact_non_college_negative(self):
        """Test the estimated impact of educ on wage for non-college graduates with negative coefficient"""
        beta0 = 10.0
        beta1 = -2.0
        beta2 = 0.5
        std_err_beta2 = 0.1
        p_value_beta2 = 0.01

        impact_non_college, impact_college, is_impact_different = estimated_impact(beta0, beta1, beta2, std_err_beta2, p_value_beta2)

        self.assertEqual(impact_non_college, -2.0)

    def test_impact_college_negative(self):
        """Test the estimated impact of educ on wage for college graduates with negative coefficient"""
        beta0 = 10.0
        beta1 = -2.0
        beta2 = 0.5
        std_err_beta2 = 0.1
        p_value_beta2 = 0.01

        impact_non_college, impact_college, is_impact_different = estimated_impact(beta0, beta1, beta2, std_err_beta2, p_value_beta2)

        self.assertEqual(impact_college, -1.5)

    def test_is_impact_different_false(self):
        """Test if the impacts for the two groups are not significantly different"""
        beta0 = 10.0
        beta1 = 2.0
        beta2 = 0.5
        std_err_beta2 = 0.1
        p_value_beta2 = 0.1

        impact_non_college, impact_college, is_impact_different = estimated_impact(beta0, beta1, beta2, std_err_beta2, p_value_beta2)

        self.assertFalse(is_impact_different)

if __name__ == '__main__':
    unittest.main()
