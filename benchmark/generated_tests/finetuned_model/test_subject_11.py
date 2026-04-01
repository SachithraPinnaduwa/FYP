import unittest

class TestExtractFileInfo(unittest.TestCase):

    def test_valid_input(self):
        # Test with a valid input string
        input_string = '<reponame>user/repo<filename>file.py'
        expected_output = {
            'repository_name': 'repo',
            'author_username': 'user',
            'file_name': 'file.py'
        }
        self.assertEqual(extract_file_info(input_string), expected_output)

    def test_author_username_with_hyphen(self):
        # Test with an author username containing a hyphen
        input_string = '<reponame>user-name/repo<filename>file.py'
        expected_output = {
            'repository_name': 'repo',
            'author_username': 'user-name',
            'file_name': 'file.py'
        }
        self.assertEqual(extract_file_info(input_string), expected_output)

    def test_repository_name_with_hyphen(self):
        # Test with a repository name containing a hyphen
        input_string = '<reponame>user/repo-name<filename>file.py'
        expected_output = {
            'repository_name': 'repo-name',
            'author_username': 'user',
            'file_name': 'file.py'
        }
        self.assertEqual(extract_file_info(input_string), expected_output)

    def test_file_name_with_extension(self):
        # Test with a file name containing an extension
        input_string = '<reponame>user/repo<filename>file.txt'
        expected_output = {
            'repository_name': 'repo',
            'author_username': 'user',
            'file_name': 'file.txt'
        }
        self.assertEqual(extract_file_info(input_string), expected_output)

    def test_no_file_name(self):
        # Test with no file name
        input_string = '<reponame>user/repo<filename>'
        self.assertIsNone(extract_file_info(input_string))

    def test_no_author_username(self):
        # Test with no author username
        input_string = '<reponame>/repo<filename>file.py'
        self.assertIsNone(extract_file_info(input_string))

    def test_no_repository_name(self):
        # Test with no repository name
        input_string = '<reponame>user/<filename>file.py'
        self.assertIsNone(extract_file_info(input_string))