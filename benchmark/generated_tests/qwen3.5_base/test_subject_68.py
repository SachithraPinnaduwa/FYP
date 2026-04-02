import unittest

class TestExtractDivAttributes(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(extract_div_attributes(""), [])

    def test_single_div(self):
        html = '<div class="test" id="myDiv">Content</div>'
        expected = [{'class': 'test', 'id': 'myDiv'}]
        self.assertEqual(extract_div_attributes(html), expected)

    def test_multiple_divs(self):
        html = '<div class="a" id="1">A</div><div class="b" id="2">B</div>'
        expected = [{'class': 'a', 'id': '1'}, {'class': 'b', 'id': '2'}]
        self.assertEqual(extract_div_attributes(html), expected)

    def test_div_with_no_attributes(self):
        html = '<div>Content</div>'
        expected = []
        self.assertEqual(extract_div_attributes(html), expected)

    def test_div_with_single_attribute(self):
        html = '<div class="test">Content</div>'
        expected = [{'class': 'test'}]
        self.assertEqual(extract_div_attributes(html), expected)

    def test_div_with_multiple_attributes(self):
        html = '<div class="test" id="myDiv" data-value="123">Content</div>'
        expected = [{'class': 'test', 'id': 'myDiv', 'data-value': '123'}]
        self.assertEqual(extract_div_attributes(html), expected)

    def test_div_with_special_characters_in_attribute_value(self):
        html = '<div class="test" data-value="value with spaces">Content</div>'
        expected = [{'class': 'test', 'data-value': 'value with spaces'}]
        self.assertEqual(extract_div_attributes(html), expected)

    def test_div_with_newline_in_attribute_value(self):
        html = '<div class="test" data-value="value\nwith\nnewlines">Content</div>'
        expected = [{'class': 'test', 'data-value': 'value\nwith\nnewlines'}]
        self.assertEqual(extract_div_attributes(html), expected)

    def test_div_with_tab_in_attribute_value(self):
        html = '<div class="test" data-value="value\twith\ttabs">Content</div>'
        expected = [{'class': 'test', 'data-value': 'value\twith\ttabs'}]
        self.assertEqual(extract_div_attributes(html), expected)

    def test_div_with_unicode_in_attribute_value(self):
        html = '<div class="test" data-value="value with unicode: 你好世界">Content</div>'
        expected = [{'class': 'test', 'data-value': 'value with unicode: 你好世界'}]
        self.assertEqual(extract_div_attributes(html), expected)

    def test_div_with_attribute_value_containing_equal_sign(self):
        html = '<div class="test" data-value="value=with=equals">Content</div>'
        expected = [{'class': 'test', 'data-value': 'value=with=equals'}]
        self.assertEqual(extract_div_attributes(html), expected)

    def test_div_with_attribute_value_containing_quote(self):
        html = '<div class="test" data-value="value with "">Content</div>'
        expected = [{'class': 'test', 'data-value': 'value with ""'}]
        self.assertEqual(extract_div_attributes(html), expected)

    def test_div_with_attribute_value_containing_newline(self):
        html = '<div class="test" data-value="value\nwith\nnewlines">Content</div>'
        expected = [{'class': 'test', 'data-value': 'value\nwith\nnewlines'}]
        self.assertEqual(extract_div_attributes(html), expected)

    def test_div_with_attribute_value_containing_tab(self):
        html = '<div class="test" data-value="value\twith\ttabs">Content</div>'
        expected = [{'class': 'test', 'data-value': 'value\twith\ttabs'}]
        self.assertEqual(extract_div_attributes(html), expected)

    def test_div_with_attribute_value_containing_unicode(self):
        html = '<div class="test" data-value="value with unicode: 你好世界">Content</div>'
        expected = [{'class': 'test', 'data-value': 'value with unicode: 你好世界'}]
        self.assertEqual(extract_div_attributes(html), expected)

    def test_div_with_attribute_value_containing_equal_sign(self):
        html = '<div class="test" data-value="value=with=equals">Content</div>'
        expected = [{'class': 'test', 'data-value': 'value=with=equals'}]
        self.assertEqual(extract_div_attributes(html), expected)

    def test_div_with_attribute_value_containing_quote(self):
        html = '<div class="test" data-value="value with "">Content</div>'
        expected = [{'class': 'test', 'data-value': 'value with ""'}]
        self.assertEqual(extract_div_attributes(html), expected)

    def test_div_with_attribute_value_containing_newline(self):
        html = '<div class="test" data-value="value\nwith\nnewlines">Content</div>'
        expected = [{'class': 'test', 'data-value': 'value\nwith\nnewlines'}]
        self.assertEqual(extract_div_attributes(html), expected)

    def test_div_with_attribute_value_containing_tab(self):
        html = '<div class="test" data-value="value\twith\ttabs">Content</div>'
        expected = [{'class': 'test', 'data-value': 'value\twith\ttabs'}]
        self.assertEqual(extract_div_attributes(html), expected)

    def test_div_with_attribute_value_containing_unicode(self):
        html = '<div class="test" data-value="value with unicode: 你好世界">Content</div>'
        expected = [{'class': 'test', 'data-value': 'value with unicode: 你好世界'}]
        self.assertEqual(extract_div_attributes(html), expected)

if __name__ == '__main__':
    unittest.main()
