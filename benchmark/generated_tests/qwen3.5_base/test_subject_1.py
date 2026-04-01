import unittest

class TestSimpleLogParser(unittest.TestCase):
    def setUp(self):
        self.parser = SimpleLogParser("test_logs.txt")

    def test_load_and_parse(self):
        self.parser.load_and_parse()
        self.assertEqual(len(self.parser.entries), 3)
        self.assertEqual(self.parser.entries[0].level, "INFO")
        self.assertEqual(self.parser.entries[1].level, "WARNING")
        self.assertEqual(self.parser.entries[2].level, "ERROR")

    def test_filter_levels(self):
        self.parser.load_and_parse(filter_levels=["ERROR"])
        self.assertEqual(len(self.parser.entries), 1)
        self.assertEqual(self.parser.entries[0].level, "ERROR")

    def test_get_errors_by_component(self):
        self.parser.load_and_parse()
        errors = self.parser.get_errors_by_component()
        self.assertIn("database", errors)
        self.assertIn("auth", errors)
        self.assertEqual(errors["database"], 1)
        self.assertEqual(errors["auth"], 1)

if __name__ == "__main__":
    unittest.main()
