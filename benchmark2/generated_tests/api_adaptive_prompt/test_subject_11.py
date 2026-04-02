from subject_11 import *

import unittest

def extract_file_info(input_string):
    match = re.match(r'<reponame>(?P<author_username>[\w-]+)/(?P<repository_name>[\w-]+)<filename>(?P<file_name>.+)', input_string)
    if match:
        return {
            'repository_name': match.group('repository_name'),
            'author_username': match.group('author_username'),
            'file_name': match.group('file_name')
        }
    else:
        return None

class TestExtractFileInfo(unittest.TestCase):
    def test_normal_case(self):
        input_string = '<reponame>username/repo<filename>file.py'
        expected_output = {'repository_name': 'repo', 'author_username': 'username', 'file_name': 'file.py'}
        self.assertEqual(extract_file_info(input_string), expected_output)

    def test_edge_case_no_filename(self):
        input_string = '<reponame>username/repo<filename>'
        expected_output = {'repository_name': 'repo', 'author_username': 'username', 'file_name': None}
        self.assertEqual(extract_file_info(input_string), expected_output)

    def test_error_handling_invalid_format(self):
        input_string = '<reponame>username/repo<filename>invalid_file_name'
        expected_output = None
        self.assertEqual(extract_file_info(input_string), expected_output)

if __name__ == '__main__':
    unittest.main()