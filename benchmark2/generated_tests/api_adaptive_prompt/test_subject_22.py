from subject_22 import *

import unittest
from typing import List
import os

def find_python_files(directory_path: str) -> List[str]:
    python_files = []

    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith(".py"):
                python_files.append(os.path.join(root, file))

    return python_files

class TestFindPythonFiles(unittest.TestCase):
    def test_normal_case(self):
        # Create a temporary directory with Python files
        import tempfile
        with tempfile.TemporaryDirectory() as temp_dir:
            # Create some Python files
            with open(os.path.join(temp_dir, 'test1.py'), 'w') as f:
                f.write('print("Hello, World!")')
            with open(os.path.join(temp_dir, 'test2.py'), 'w') as f:
                f.write('print("Another Python file")')
            # Create a subdirectory with a Python file
            sub_dir = os.path.join(temp_dir, 'subdir')
            os.mkdir(sub_dir)
            with open(os.path.join(sub_dir, 'test3.py'), 'w') as f:
                f.write('print("Subdirectory Python file")')

            # Call the function and check the result
            result = find_python_files(temp_dir)
            expected = [
                os.path.join(temp_dir, 'test1.py'),
                os.path.join(temp_dir, 'test2.py'),
                os.path.join(sub_dir, 'test3.py')
            ]
            self.assertEqual(result, expected)

    def test_edge_case_empty_directory(self):
        # Create a temporary empty directory
        import tempfile
        with tempfile.TemporaryDirectory() as temp_dir:
            # Call the function and check the result
            result = find_python_files(temp_dir)
            expected = []
            self.assertEqual(result, expected)

    def test_edge_case_non_existent_directory(self):
        # Create a non-existent directory path
        non_existent_dir = '/path/to/non-existent/directory'

        # Call the function and check that it raises a FileNotFoundError
        with self.assertRaises(FileNotFoundError):
            find_python_files(non_existent_dir)

    def test_error_handling_non_string_input(self):
        # Call the function with a non-string input and check that it raises a TypeError
        with self.assertRaises(TypeError):
            find_python_files(123)
        with self.assertRaises(TypeError):
            find_python_files(['string', 'list'])

if __name__ == '__main__':
    unittest.main()