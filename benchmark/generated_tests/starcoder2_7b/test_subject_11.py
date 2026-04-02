import unittest

class TestExtractFileInfo(unittest.TestCase):
    def test_extract_file_info(self):
        self.assertEqual(extract_file_info('<reponame>github/test-repo<filename>test_file.py'), {'repository_name': 'test-repo', 'author_username': 'github', 'file_name': 'test_file.py'})
        self.assertEqual(extract_file_info('<reponame>github/test-repo<filename>test_file.py'), {'repository_name': 'test-repo', 'author_username': 'github', 'file_name': 'test_file.py'})
        self.assertEqual(extract_file_info('<reponame>github/test-repo<filename>test_file.py'), {'repository_name': 'test-repo', 'author_username': 'github', 'file_name': 'test_file.py'})
        self.assertEqual(extract_file_info('<reponame>github/test-repo<filename>test_file.py'), {'repository_name': 'test-repo', 'author_username': 'github', 'file_name': 'test_file.py'})
        self.assertEqual(extract_file_info('<reponame>github/test-repo<filename>test_file.py'), {'repository_name': 'test-repo', 'author_username': 'github', 'file_name': 'test_file.py'})
        self.assertEqual(extract_file_info('<reponame>github/test-repo<filename>test_file.py'), {'repository_name': 'test-repo', 'author_username': 'github', 'file_name': 'test_file.py'})
        self.assertEqual(extract_file_info('<reponame>github/test-repo<filename>test_file.py'), {'repository_name': 'test-repo', 'author_username': 'github', 'file_name': 'test_file.py'})
        self.assertEqual(extract_file_info('<reponame>github/test-repo<filename>test_file.py'), {'repository_name': 'test-repo', 'author_username': 'github', 'file_name': 'test_file.py'})
        self.assertEqual(extract_file_info('<repon