import unittest

class TestPasswordPolicyValidator(unittest.TestCase):
    def setUp(self):
        self.validator = PasswordPolicyValidator()

    def test_valid_password(self):
        password = "SecurePass1!"
        result = self.validator.validate(password)
        self.assertTrue(result["is_valid"])
        self.assertEqual(result["errors"], [])

    def test_invalid_length(self):
        password = "Short"
        result = self.validator.validate(password)
        self.assertFalse(result["is_valid"])
        self.assertIn("Must be at least 8 characters", result["errors"])

    def test_missing_uppercase(self):
        password = "securepass1!"
        result = self.validator.validate(password)
        self.assertFalse(result["is_valid"])
        self.assertIn("Must contain uppercase", result["errors"])

    def test_missing_lowercase(self):
        password = "SECUREPASS1!"
        result = self.validator.validate(password)
        self.assertFalse(result["is_valid"])
        self.assertIn("Must contain lowercase", result["errors"])

    def test_missing_number(self):
        password = "SecurePass!"
        result = self.validator.validate(password)
        self.assertFalse(result["is_valid"])
        self.assertIn("Must contain number", result["errors"])

    def test_missing_special(self):
        password = "SecurePass1"
        result = self.validator.validate(password)
        self.assertFalse(result["is_valid"])
        self.assertIn("Must contain special character", result["errors"])

    def test_custom_policy(self):
        custom_validator = PasswordPolicyValidator(min_length=10, req_upper=True, req_lower=True, req_num=True, req_special=True)
        password = "SecurePass1!"
        result = custom_validator.validate(password)
        self.assertFalse(result["is_valid"])
        self.assertIn("Must be at least 10 characters", result["errors"])

if __name__ == '__main__':
    unittest.main()
