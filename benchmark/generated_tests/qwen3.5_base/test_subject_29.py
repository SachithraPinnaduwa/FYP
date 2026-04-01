import unittest

class TestSimpleCronParser(unittest.TestCase):
    def test_valid_cron(self):
        parser = SimpleCronParser("0 0 1 1 *")
        self.assertTrue(parser.is_time_match(0, 0, 1, 1, 0))
        self.assertFalse(parser.is_time_match(1, 0, 1, 1, 0))

    def test_invalid_cron(self):
        with self.assertRaises(ValueError):
            SimpleCronParser("0 0 1 1")

    def test_range(self):
        parser = SimpleCronParser("0 0-5 1 1 *")
        self.assertTrue(parser.is_time_match(0, 0, 1, 1, 0))
        self.assertTrue(parser.is_time_match(0, 5, 1, 1, 0))
        self.assertFalse(parser.is_time_match(0, 6, 1, 1, 0))

    def test_step(self):
        parser = SimpleCronParser("0 */2 1 1 *")
        self.assertTrue(parser.is_time_match(0, 0, 1, 1, 0))
        self.assertTrue(parser.is_time_match(0, 2, 1, 1, 0))
        self.assertFalse(parser.is_time_match(0, 1, 1, 1, 0))

    def test_list(self):
        parser = SimpleCronParser("0 0,6 1 1 *")
        self.assertTrue(parser.is_time_match(0, 0, 1, 1, 0))
        self.assertTrue(parser.is_time_match(0, 6, 1, 1, 0))
        self.assertFalse(parser.is_time_match(0, 3, 1, 1, 0))

    def test_combined(self):
        parser = SimpleCronParser("0 0-5 1,15 1,3 *")
        self.assertTrue(parser.is_time_match(0, 0, 1, 1, 0))
        self.assertTrue(parser.is_time_match(0, 5, 15, 3, 0))
        self.assertFalse(parser.is_time_match(0, 6, 1, 1, 0))

if __name__ == '__main__':
    unittest.main()
