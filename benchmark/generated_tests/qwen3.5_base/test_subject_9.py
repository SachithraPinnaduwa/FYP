import unittest

class TestConfigValidator(unittest.TestCase):
    def test_valid_config(self):
        schema = {"required": ["name", "age"]}
        validator = ConfigValidator(schema)
        config = {"name": "Alice", "age": 30}
        self.assertTrue(validator.validate(config))

    def test_missing_required_field(self):
        schema = {"required": ["name", "age"]}
        validator = ConfigValidator(schema)
        config = {"name": "Alice"}
        self.assertFalse(validator.validate(config))

    def test_non_dict_config(self):
        schema = {"required": ["name", "age"]}
        validator = ConfigValidator(schema)
        config = "Alice"
        self.assertFalse(validator.validate(config))

    def test_empty_config(self):
        schema = {"required": ["name", "age"]}
        validator = ConfigValidator(schema)
        config = {}
        self.assertFalse(validator.validate(config))

    def test_extra_fields_allowed(self):
        schema = {"required": ["name", "age"]}
        validator = ConfigValidator(schema)
        config = {"name": "Alice", "age": 30, "extra": "field"}
        self.assertTrue(validator.validate(config))

if __name__ == '__main__':
    unittest.main()
