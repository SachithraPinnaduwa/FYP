import unittest

class TestHTMLBuilder(unittest.TestCase):
    def test_p_tag(self):
        builder = HTMLBuilder()
        builder.p("Hello World")
        self.assertEqual(builder.render(), "<p>Hello World</p>")

    def test_a_tag(self):
        builder = HTMLBuilder()
        builder.a("https://example.com", "Click here")
        self.assertEqual(builder.render(), "<a href=\"https://example.com\">Click here</a>")

    def test_div_tag(self):
        builder = HTMLBuilder()
        builder.div("Content")
        self.assertEqual(builder.render(), "<div>Content</div>")

    def test_multiple_tags(self):
        builder = HTMLBuilder()
        builder.p("First")
        builder.a("https://example.com", "Second")
        builder.div("Third")
        self.assertEqual(builder.render(), "<p>First</p>\n<a href=\"https://example.com\">Second</a>\n<div>Third</div>")

    def test_tag_with_attributes(self):
        builder = HTMLBuilder()
        builder.a("https://example.com", "Link", target="_blank")
        self.assertEqual(builder.render(), "<a href=\"https://example.com\" target=\"_blank\">Link</a>")

    def test_empty_tag(self):
        builder = HTMLBuilder()
        builder.p("")
        self.assertEqual(builder.render(), "<p></p>")

    def test_complex_html(self):
        builder = HTMLBuilder()
        builder.p("Welcome to our website")
        builder.a("https://example.com", "Visit Example")
        builder.div("More content here")
        self.assertEqual(builder.render(), "<p>Welcome to our website</p>\n<a href=\"https://example.com\">Visit Example</a>\n<div>More content here</div>")

if __name__ == "__main__":
    unittest.main()
