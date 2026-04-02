import unittest

class TestExtractDivAttributes(unittest.TestCase):
    def test_extract_div_attributes(self):
        html_snippet = '<div class="container"><p>Hello, world!</p></div><div id="main" class="content"><p>Welcome to the site!</p></div>'
        expected_output = [{'class': 'container'}, {'id': 'main', 'class': 'content'}]
        self.assertEqual(extract_div_attributes(html_snippet), expected_output)

    def test_empty_html_snippet(self):
        html_snippet = ''
        expected_output = []
        self.assertEqual(extract_div_attributes(html_snippet), expected_output)

    def test_no_div_tags(self):
        html_snippet = '<p>This is a paragraph.</p>'
        expected_output = []
        self.assertEqual(extract_div_attributes(html_snippet), expected_output)

    def test_single_div_tag(self):
        html_snippet = '<div id="example" class="sample">Example content</div>'
        expected_output = [{'id': 'example', 'class': 'sample'}]
        self.assertEqual(extract_div_attributes(html_snippet), expected_output)

    def test_multiple_div_tags(self):
        html_snippet = '<div id="div1" class="class1"><p>Div 1 content</p></div><div id="div2" class="class2"><p>Div 2 content</p></div>'
        expected_output = [{'id': 'div1', 'class': 'class1'}, {'id': 'div2', 'class': 'class2'}]
        self.assertEqual(extract_div_attributes(html_snippet), expected_output)

    def test_missing_quotes(self):
        html_snippet = '<div id=example class=sample>Example content</div>'
        expected_output = [{'id': 'example', 'class': 'sample'}]
        self.assertEqual(extract_div_attributes(html_snippet), expected_output)

    def test_single_quote_values(self):
        html_snippet = '<div id=\'example\' class=\'sample\'>Example content</div>'
        expected_output = [{'id': 'example', 'class': 'sample'}]
        self.assertEqual(extract_div_attributes(html_snippet), expected_output)

    def test_multiple_attributes(self):
        html_snippet = '<div id="example" class="sample" data-role="main">Example content</div>'
        expected_output = [{'id': 'example', 'class': 'sample', 'data-role': 'main'}]
        self.assertEqual(extract_div_attributes(html_snippet), expected_output)

    def test_empty_attributes(self):
        html_snippet = '<div id="" class="">Example content</div>'
        expected_output = [{'id': '', 'class': ''}]
        self.assertEqual(extract_div_attributes(html_snippet), expected_output)

    def test_no_attributes(self):
        html_snippet = '<div>Example content</div>'
        expected_output = [{'id': '', 'class': ''}]
        self.assertEqual(extract_div_attributes(html_snippet), expected_output)

if __name__ == '__main__':
    unittest.main()