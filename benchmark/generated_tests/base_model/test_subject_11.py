import unittest
from extract_file_info import extract_file_info

class TestExtractFileInfo(unittest.TestCase):

    def test_valid_input(self):
        input_string = '<reponame>johndoe/my-project<filename>main.py'
        expected_output = {'repository_name': 'my-project', 'author_username': 'johndoe', 'file_name': 'main.py'}
        self.assertEqual(extract_file_info(input_string), expected_output)

    def test_invalid_format(self):
        input_string = '<reponame>johndoe/my-project/main.py'
        expected_output = None
        self.assertEqual(extract_file_info(input_string), expected_output)

    def test_empty_input(self):
        input_string = ''
        expected_output = None
        self.assertEqual(extract_file_info(input_string), expected_output)

    def test_no_filename(self):
        input_string = '<reponame>johndoe/my-project<filename>'
        expected_output = None
        self.assertEqual(extract_file_info(input_string), expected_output)

    def test_special_characters_in_filename(self):
        input_string = '<reponame>johndoe/my-project<filename>readme.md'
        expected_output = {'repository_name': 'my-project', 'author_username': 'johndoe', 'file_name': 'readme.md'}
        self.assertEqual(extract_file_info(input_string), expected_output)

    def test_leading_trailing_whitespace(self):
        input_string = '  <reponame>johndoe/my-project<filename> main.py  '
        expected_output = {'repository_name': 'my-project', 'author_username': 'johndoe', 'file_name': 'main.py'}
        self.assertEqual(extract_file_info(input_string), expected_output)

if __name__ == '__main__':
    unittest.main()