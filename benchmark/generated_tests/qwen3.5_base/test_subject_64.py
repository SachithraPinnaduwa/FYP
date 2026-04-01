import unittest

class TestBasicAuthHeaderHelper(unittest.TestCase):
    def setUp(self):
        self.helper = BasicAuthHeaderHelper()

    def test_create_header(self):
        self.assertEqual(self.helper.create_header("user", "pass"), "Basic dXNlcjpwYXNz")

    def test_create_header_with_special_chars(self):
        self.assertEqual(self.helper.create_header("user@domain.com", "pass123!"), "Basic dXNlckBkb21haW4uY29tOnBhc3EyMjMh")

    def test_create_header_with_unicode(self):
        self.assertEqual(self.helper.create_header("user", "пароль"), "Basic dXNlcj60YXJzb24=")

    def test_create_header_with_empty_password(self):
        self.assertEqual(self.helper.create_header("user", ""), "Basic dXNlcjo=")

    def test_create_header_with_empty_username(self):
        self.assertEqual(self.helper.create_header("", "pass"), "Basic OgBhc3M=")

    def test_create_header_with_whitespace(self):
        self.assertEqual(self.helper.create_header("user ", " pass"), "Basic dXNlcjogcGFzcw==")

    def test_create_header_with_newline(self):
        self.assertEqual(self.helper.create_header("user\n", "pass\n"), "Basic dXNlcj4KcGFzcw==")

    def test_create_header_with_tab(self):
        self.assertEqual(self.helper.create_header("user\t", "pass\t"), "Basic dXNlcjx0cGFzcw==")

    def test_create_header_with_control_chars(self):
        self.assertEqual(self.helper.create_header("user\x00", "pass\x01"), "Basic dXNlcj4wMDE=")

    def test_create_header_with_long_password(self):
        self.assertEqual(self.helper.create_header("user", "a" * 1000), "Basic dXNlcjphYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNlYXNl