import unittest
from typing import List, Dict
from extract_div_attributes import extract_div_attributes

class TestExtractDivAttributes(unittest.TestCase):

    def test_single_div_no_attributes(self):
        html = '<div></div>'
        expected = [{'': ''}]
        self.assertEqual(extract_div_attributes(html), expected)

    def test_single_div_with_attributes(self):
        html = '<div id="main" class="container"></div>'
        expected = [{'id': 'main', 'class': 'container'}]
        self.assertEqual(extract_div_attributes(html), expected)

    def test_multiple_divs_with_attributes(self):
        html = '<div id="header"></div><div class="content"></div>'
        expected = [{'id': 'header'}, {'class': 'content'}]
        self.assertEqual(extract_div_attributes(html), expected)

    def test_div_with_single_quoted_attributes(self):
        html = "<div id='main' class='container'></div>"
        expected = [{'id': 'main', 'class': 'container'}]
        self.assertEqual(extract_div_attributes(html), expected)

    def test_div_with_mixed_quotes(self):
        html = '<div id="main" class=\'container\' style="color: red;"></div>'
        expected = [{'id': 'main', 'class': 'container', 'style': 'color: red;'}]
        self.assertEqual(extract_div_attributes(html), expected)

    def test_div_with_missing_quote(self):
        html = '<div id="main" class="container style="color: red;">'
        expected = [{'id': 'main', 'class': 'container'}]
        self.assertEqual(extract_div_attributes(html), expected)

    def test_empty_string_input(self):
        html = ''
        expected = []
        self.assertEqual(extract_div_attributes(html), expected)

    def test_no_div_tags(self):
        html = '<p>This is a paragraph.</p>'
        expected = []
        self.assertEqual(extract_div_attributes(html), expected)

if __name__ == '__main__':
    unittest.main()