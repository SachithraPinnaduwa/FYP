from subject_68 import *

import unittest
from typing import List, Dict
import re

def extract_div_attributes(html_snippet: str) -> List[Dict[str, str]]:
    div_attributes = []
    div_pattern = re.compile(r'<div\s+([^>]+)>')
    attribute_pattern = re.compile(r'(\w+)\s*=\s*["\']([^"\']+)["\']')

    div_matches = div_pattern.findall(html_snippet)
    for match in div_matches:
        attributes = {}
        attribute_matches = attribute_pattern.findall(match)
        for attr, value in attribute_matches:
            attributes[attr] = value
        div_attributes.append(attributes)

    return div_attributes

class TestExtractDivAttributes(unittest.TestCase):
    def test_extract_div_attributes(self):
        html_snippet = '<div class="container" id="main"><div class="content" id="content1">Content 1</div><div class="content" id="content2">Content 2</div></div>'
        expected_output = [{'class': 'container', 'id': 'main'}, {'class': 'content', 'id': 'content1'}, {'class': 'content', 'id': 'content2'}]
        self.assertEqual(extract_div_attributes(html_snippet), expected_output)

    def test_extract_div_attributes_no_attributes(self):
        html_snippet = '<div><div>Content</div></div>'
        expected_output = [{}, {}]
        self.assertEqual(extract_div_attributes(html_snippet), expected_output)

    def test_extract_div_attributes_single_attribute(self):
        html_snippet = '<div class="container"><div>Content</div></div>'
        expected_output = [{'class': 'container'}, {}]
        self.assertEqual(extract_div_attributes(html_snippet), expected_output)

    def test_extract_div_attributes_multiple_classes(self):
        html_snippet = '<div class="container main"><div>Content</div></div>'
        expected_output = [{'class': 'container main'}, {}]
        self.assertEqual(extract_div_attributes(html_snippet), expected_output)

    def test_extract_div_attributes_single_quoted_attributes(self):
        html_snippet = '<div class=\'container\' id=\'main\'><div class=\'content\' id=\'content1\'>Content 1</div><div class=\'content\' id=\'content2\'>Content 2</div></div>'
        expected_output = [{'class': 'container', 'id': 'main'}, {'class': 'content', 'id': 'content1'}, {'class': 'content', 'id': 'content2'}]
        self.assertEqual(extract_div_attributes(html_snippet), expected_output)

    def test_extract_div_attributes_no_div_tags(self):
        html_snippet = '<p>Paragraph</p>'
        expected_output = []
        self.assertEqual(extract_div_attributes(html_snippet), expected_output)

if __name__ == '__main__':
    unittest.main()