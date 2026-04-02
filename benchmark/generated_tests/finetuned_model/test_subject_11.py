import unittest

class TestExtractFileInfo(unittest.TestCase):
    def test_extract_file_info(self):
        self.assertEqual(extract_file_info('<reponame>user/repo<filename>file.py'), 
                         {'repository_name': 'repo', 'author_username': 'user', 'file_name': 'file.py'})
        self.assertEqual(extract_file_info('<reponame>user/another_repo<filename>test.txt'), 
                         {'repository_name': 'another_repo', 'author_username': 'user', 'file_name': 'test.txt'})
        self.assertEqual(extract_file_info('<reponame>user/last_repo<filename>main.c'), 
                         {'repository_name': 'last_repo', 'author_username': 'user', 'file_name': 'main.c'})
        self.assertIsNone(extract_file_info('<reponame>user/repo<filename>'))
        self.assertIsNone(extract_file_info('<reponame>user<filename>file.py'))
        self.assertIsNone(extract_file_info('<reponame><filename>file.py'))
        self.assertIsNone(extract_file_info(''))

if __name__ == '__main__':
    unittest.main()