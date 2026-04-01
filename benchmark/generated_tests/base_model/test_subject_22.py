import unittest
from typing import List
from pathlib import Path
import os

# Assuming the function is defined in a module named 'file_finder'
from file_finder import find_python_files

class TestFindPythonFiles(unittest.TestCase):

    def setUp(self):
        # Create a temporary directory structure for testing
        self.temp_dir = Path('temp_test_dir')
        self.temp_dir.mkdir(exist_ok=True)
        
        # Create some Python files and non-Python files
        self.python_file1 = self.temp_dir / 'test1.py'
        self.python_file2 = self.temp_dir / 'subdir' / 'test2.py'
        self.non_python_file = self.temp_dir / 'non_python.txt'
        
        self.python_file1.touch()
        self.python_file2.parent.mkdir(parents=True, exist_ok=True)
        self.python_file2.touch()
        self.non_python_file.touch()

    def tearDown(self):
        # Clean up the temporary directory after each test
        for item in self.temp_dir.iterdir():
            if item.is_dir():
                item.rmdir()
            else:
                item.unlink()
        self.temp_dir.rmdir()

    def test_find_python_files_in_single_directory(self):
        result = find_python_files(str(self.temp_dir))
        expected = [str(self.python_file1), str(self.python_file2)]
        self.assertEqual(sorted(result), sorted(expected))

    def test_find_python_files_in_subdirectory(self):
        result = find_python_files(str(self.temp_dir / 'subdir'))
        expected = [str(self.python_file2)]
        self.assertEqual(sorted(result), sorted(expected))

    def test_find_python_files_no_files(self):
        empty_dir = self.temp_dir / 'empty_dir'
        empty_dir.mkdir(exist_ok=True)
        result = find_python_files(str(empty_dir))
        self.assertEqual(result, [])

    def test_find_python_files_nonexistent_directory(self):
        nonexistent_dir = self.temp_dir / 'nonexistent_dir'
        with self.assertRaises(FileNotFoundError):
            find_python_files(str(nonexistent_dir))

if __name__ == '__main__':
    unittest.main()