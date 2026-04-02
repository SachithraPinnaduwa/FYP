from subject_68 import *

import unittest

class TestExtractDivAttributes(unittest.TestCase):
    def test_normal_case_single_div_tag(self):
        html_snippet = '<div id="example" class="container" style="color: red;">Content</div>'
        expected = [{'id': 'example', 'class': 'container', 'style': 'color: red;'}]
        self.assertEqual(extract_div_attributes(html_snippet), expected)

    def test_normal_case_multiple_div_tags(self):
        html_snippet = '<div id="example1" class="container1">Content1</div><div id="example2" style="color: blue;">Content2</div>'
        expected = [{'id': 'example1', 'class': 'container1'}, {'id': 'example2', 'style': 'color: blue;'}]
        self.assertEqual(extract_div_attributes(html_snippet), expected)

    def test_normal_case_div_tag_no_attributes(self):
        html_snippet = '<div>Content</div>'
        expected = [{'class': ''}]
        self.assertEqual(extract_div_attributes(html_snippet), expected)

    def test_error_handling_empty_input(self):
        html_snippet = ''
        expected = []
        self.assertEqual(extract_div_attributes(html_snippet), expected)

    def test_error_handling_div_tag_missing_quotes(self):
        html_snippet = '<div id=example>Content</div>'
        expected = [{'id': 'example'}]
        self.assertEqual(extract_div_attributes(html_snippet), expected)

if __name__ == '__main__':
    unittest.main()