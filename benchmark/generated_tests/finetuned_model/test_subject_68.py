import unittest

class TestExtractDivAttributes(unittest.TestCase):

    def test_single_div_tag(self):
        # Test case with a single div tag
        html_snippet = '<div class="example" id="123"></div>'
        expected_output = [{'class': 'example', 'id': '123'}]
        self.assertEqual(extract_div_attributes(html_snippet), expected_output)

    def test_multiple_div_tags(self):
        # Test case with multiple div tags
        html_snippet = '<div class="example" id="123"></div><div class="test" id="456"></div>'
        expected_output = [{'class': 'example', 'id': '123'}, {'class': 'test', 'id': '456'}]
        self.assertEqual(extract_div_attributes(html_snippet), expected_output)

    def test_no_attributes(self):
        # Test case with a div tag that has no attributes
        html_snippet = '<div></div>'
        expected_output = [{}]
        self.assertEqual(extract_div_attributes(html_snippet), expected_output)

    def test_attributes_with_single_quotes(self):
        # Test case with attributes enclosed in single quotes
        html_snippet = '<div class=\'example\' id=\'123\'></div>'
        expected_output = [{'class': 'example', 'id': '123'}]
        self.assertEqual(extract_div_attributes(html_snippet), expected_output)

    def test_attributes_with_no_values(self):
        # Test case with attributes that have no values
        html_snippet = '<div class id="123"></div>'
        expected_output = [{'class': '', 'id': '123'}]
        self.assertEqual(extract_div_attributes(html_snippet), expected_output)

    def test_attributes_with_extra_spaces(self):
        # Test case with attributes that have extra spaces
        html_snippet = '<div class="example" id ="123" ></div>'
        expected_output = [{'class': 'example', 'id': '123'}]
        self.assertEqual(extract_div_attributes(html_snippet), expected_output)

    def test_attributes_with_special_characters(self):
        # Test case with attributes that have special characters
        html_snippet = '<div class="example_123" id="456"></div>'
        expected_output = [{'class': 'example_123', 'id': '456'}]
        self.assertEqual(extract_div_attributes(html_snippet), expected_output)