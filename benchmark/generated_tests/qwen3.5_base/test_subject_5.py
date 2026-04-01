import unittest

class TestMarkdownParser(unittest.TestCase):
    def test_bold(self):
        self.assertEqual(MarkdownParser().parse("**bold**"), "<strong>bold</strong>")

    def test_italic(self):
        self.assertEqual(MarkdownParser().parse("*italic*"), "<em>italic</em>")

    def test_header(self):
        self.assertEqual(MarkdownParser().parse("# Header"), "<h1>Header</h1>")

    def test_multiple(self):
        self.assertEqual(MarkdownParser().parse("**bold** and *italic*"), "<strong>bold</strong> and <em>italic</em>")

    def test_no_match(self):
        self.assertEqual(MarkdownParser().parse("no match"), "no match")

    def test_empty_string(self):
        self.assertEqual(MarkdownParser().parse(""), "")

    def test_newline(self):
        self.assertEqual(MarkdownParser().parse("line1\n**bold**\nline2"), "line1\n<strong>bold</strong>\nline2")

    def test_multiple_headers(self):
        self.assertEqual(MarkdownParser().parse("# Header 1\n# Header 2"), "<h1>Header 1</h1>\n<h1>Header 2</h1>")

    def test_mixed(self):
        self.assertEqual(MarkdownParser().parse("**bold** and *italic* and # Header"), "<strong>bold</strong> and <em>italic</em> and <h1>Header</h1>")

if __name__ == '__main__':
    unittest.main()
