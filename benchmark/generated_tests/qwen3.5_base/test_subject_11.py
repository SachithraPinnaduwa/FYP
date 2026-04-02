import unittest

class TestExtractFileInfo(unittest.TestCase):
    def test_valid_input(self):
        input_string = '<reponame>john_doe/my-repo<filename>test.py'
        expected = {
            'repository_name': 'my-repo',
            'author_username': 'john_doe',
            'file_name': 'test.py'
        }
        result = extract_file_info(input_string)
        self.assertEqual(result, expected)

    def test_invalid_input(self):
        input_string = 'invalid input'
        result = extract_file_info(input_string)
        self.assertIsNone(result)

    def test_multiple_spaces(self):
        input_string = '<reponame>john_doe/my-repo<filename>  test.py  '
        expected = {
            'repository_name': 'my-repo',
            'author_username': 'john_doe',
            'file_name': 'test.py'
        }
        result = extract_file_info(input_string)
        self.assertEqual(result, expected)

    def test_special_characters_in_file_name(self):
        input_string = '<reponame>john_doe/my-repo<filename>test_file(1).py'
        expected = {
            'repository_name': 'my-repo',
            'author_username': 'john_doe',
            'file_name': 'test_file(1).py'
        }
        result = extract_file_info(input_string)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
