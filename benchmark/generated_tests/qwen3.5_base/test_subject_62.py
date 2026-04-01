import unittest

class TestFeatureToggle(unittest.TestCase):
    def setUp(self):
        self.toggle = FeatureToggle()

    def test_register_feature(self):
        self.toggle.register_feature("dark_mode", 50.0)
        self.assertEqual(self.toggle.features["dark_mode"], 50.0)

    def test_register_feature_invalid_percentage(self):
        with self.assertRaises(ValueError):
            self.toggle.register_feature("invalid_feature", -1.0)
        with self.assertRaises(ValueError):
            self.toggle.register_feature("invalid_feature", 101.0)

    def test_is_enabled_zero_percentage(self):
        self.toggle.register_feature("disabled_feature", 0.0)
        self.assertFalse(self.toggle.is_enabled("disabled_feature", "user1"))

    def test_is_enabled_hundred_percentage(self):
        self.toggle.register_feature("enabled_feature", 100.0)
        self.assertTrue(self.toggle.is_enabled("enabled_feature", "user1"))

    def test_is_enabled_random_percentage(self):
        self.toggle.register_feature("random_feature", 75.0)
        # Test with a user that should be enabled
        self.assertTrue(self.toggle.is_enabled("random_feature", "user1"))
        # Test with a user that should be disabled
        self.assertFalse(self.toggle.is_enabled("random_feature", "user2"))

    def test_is_enabled_unknown_feature(self):
        self.assertFalse(self.toggle.is_enabled("unknown_feature", "user1"))

if __name__ == '__main__':
    unittest.main()
