import unittest

class TestSimpleMarkdownFormatter(unittest.TestCase):
    def test_add_header(self):
        formatter = SimpleMarkdownFormatter()
        formatter.add_header("Test Header", 2)
        self.assertEqual(formatter.blocks, ["## Test Header"])

    def test_add_paragraph(self):
        formatter = SimpleMarkdownFormatter()
        formatter.add_paragraph("This is a paragraph.")
        self.assertEqual(formatter.blocks, ["This is a paragraph."])

    def test_add_list_ordered(self):
        formatter = SimpleMarkdownFormatter()
        formatter.add_list(["Item 1", "Item 2"], ordered=True)
        self.assertEqual(formatter.blocks, ["1. Item 1", "2. Item 2"])

    def test_add_list_unordered(self):
        formatter = SimpleMarkdownFormatter()
        formatter.add_list(["Item 1", "Item 2"], ordered=False)
        self.assertEqual(formatter.blocks, ["- Item 1", "- Item 2"])

    def test_add_code_block(self):
        formatter = SimpleMarkdownFormatter()
        formatter.add_code_block("print('Hello')", "python")
        self.assertEqual(formatter.blocks, ["