from subject_11 import *

import unittest
import re

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
    def test_extract_file_info(self):
        self.assertEqual(extract_file_info('<reponame>user/repo<filename>file.txt'), {'repository_name': 'repo', 'author_username': 'user', 'file_name': 'file.txt'})
        self.assertEqual(extract_file_info('<reponame>user/repo<filename>another_file.py'), {'repository_name': 'repo', 'author_username': 'user', 'file_name': 'another_file.py'})
        self.assertEqual(extract_file_info('<reponame>user/repo<filename>test_case_123'), {'repository_name': 'repo', 'author_username': 'user', 'file_name': 'test_case_123'})
        self.assertEqual(extract_file_info('<reponame>user/repo<filename>'), None)
        self.assertEqual(extract_file_info('<reponame>user/repo<filename>file'), None)
        self.assertEqual(extract_file_info('<reponame>user/repo<filename>file.txt<filename>'), None)
        self.assertEqual(extract_file_info('<reponame>user/repo<filename>file.txt<filename>another_file.py'), None)
        self.assertEqual(extract_file_info('<reponame>user/repo<filename>file.txt<filename>test_case_123'), None)
        self.assertEqual(extract_file_info('<reponame>user/repo<filename>file.txt<filename>file.py<filename>'), None)
        self.assertEqual(extract_file_info('<reponame>user/repo<filename>file.txt<filename>file.py<filename>another_file.py'), None)
        self.assertEqual(extract_file_info('<reponame>user/repo<filename>file.txt<filename>file.py<filename>test_case_123'), None)
        self.assertEqual(extract_file_info('<reponame>user/repo<filename>file.txt<filename>file.py<filename>file.txt'), None)
        self.assertEqual(extract_file_info('<reponame>user/repo<filename>file.txt<filename>file.py<filename>file.txt<filename>'), None)
        self.assertEqual(extract_file_info('<reponame>user/repo<filename>file.txt<filename>file.py<filename>file.txt<filename>another_file.py'), None)
        self.assertEqual(extract_file_info('<reponame>user/repo<filename>file.txt<filename>file.py<filename>file.txt<filename>test_case_123'), None)
        self.assertEqual(extract_file_info('<reponame>user/repo<filename>file.txt<filename>file.py<filename>file.txt<filename>file.py'), None)
        self.assertEqual(extract_file_info('<reponame>user/repo<filename>file.txt<filename>file.py<filename>file.txt<filename>file.py<filename>'), None)
        self.assertEqual(extract_file_info('<reponame>user/repo<filename>file.txt<filename>file.py<filename>file.txt<filename>file.py<filename>another_file.py'), None)
        self.assertEqual(extract_file_info('<reponame>user/repo<filename>file.txt<filename>file.py<filename>file.txt<filename>file.py<filename>test_case_123'), None)
        self.assertEqual(extract_file_info('<reponame>user/repo<filename>file.txt<filename>file.py<filename>file.txt<filename>file.py<filename>file.txt'), None)
        self.assertEqual(extract_file_info('<reponame>user/repo<filename>file.txt<filename>file.py<filename>file.txt<filename>file.py<filename>file.txt<filename>'), None)
        self.assertEqual(extract_file_info('<reponame>user/repo<filename>file.txt<filename>file.py<filename>file.txt<filename>file.py<filename>file.txt<filename>another_file.py'), None)
        self.assertEqual(extract_file_info('<reponame>user/repo<filename>file.txt<filename>file.py<filename>file.txt<filename>file.py<filename>file.txt<filename>test_case_123'), None)
        self.assertEqual(extract_file_info('<reponame>user/repo<filename>file.txt