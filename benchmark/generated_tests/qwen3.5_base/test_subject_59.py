import unittest

class TestHTMLSanitizer(unittest.TestCase):
    def test_basic_sanitization(self):
        input_html = "<p>Hello <b>World</b>!</p>"
        expected_output = "<p>Hello <b>World</b>!</p>"
        self.assertEqual(HTMLSanitizer().sanitize(input_html), expected_output)

    def test_script_tag_removal(self):
        input_html = "<p>Hello</p><script>alert('XSS')</script><p>World</p>"
        expected_output = "<p>Hello</p><p>World</p>"
        self.assertEqual(HTMLSanitizer().sanitize(input_html), expected_output)

    def test_attribute_stripping(self):
        input_html = "<a href='https://example.com' class='link'>Click</a>"
        expected_output = "<a>Click</a>"
        self.assertEqual(HTMLSanitizer().sanitize(input_html), expected_output)

    def test_unallowed_tag_removal(self):
        input_html = "<p>Hello <div>World</div></p>"
        expected_output = "<p>Hello </p>"
        self.assertEqual(HTMLSanitizer().sanitize(input_html), expected_output)

    def test_case_insensitivity(self):
        input_html = "<p>Hello <B>World</B>!</p>"
        expected_output = "<p>Hello <b>World</b>!</p>"
        self.assertEqual(HTMLSanitizer().sanitize(input_html), expected_output)

    def test_nested_tags(self):
        input_html = "<p>Hello <b><i>World</i></b></p>"
        expected_output = "<p>Hello <b><i>World</i></b></p>"
        self.assertEqual(HTMLSanitizer().sanitize(input_html), expected_output)

    def test_empty_input(self):
        input_html = ""
        expected_output = ""
        self.assertEqual(HTMLSanitizer().sanitize(input_html), expected_output)

    def test_mixed_content(self):
        input_html = "<p>Hello <b>World</b> <script>alert('XSS')</script> <a href='https://example.com'>Link</a></p>"
        expected_output = "<p>Hello <b>World</b> <a>Link</a></p>"
        self.assertEqual(HTMLSanitizer().sanitize(input_html), expected_output)

if __name__ == '__main__':
    unittest.main()
