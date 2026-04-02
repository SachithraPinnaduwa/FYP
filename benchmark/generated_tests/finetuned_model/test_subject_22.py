import os
import tempfile
from typing import List
from unittest import TestCase, main

class TestFindPythonFiles(TestCase):
    def test_empty_directory(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            result = find_python_files(tmpdir)
            self.assertEqual(result, [])

    def test_single_python_file(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            python_file_path = os.path.join(tmpdir, 'test.py')
            with open(python_file_path, 'w') as f:
                f.write('print("Hello, World!")')
            result = find_python_files(tmpdir)
            self.assertEqual(result, [python_file_path])

    def test_multiple_python_files(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            python_file1_path = os.path.join(tmpdir, 'test1.py')
            python_file2_path = os.path.join(tmpdir, 'subdir', 'test2.py')
            with open(python_file1_path, 'w') as f:
                f.write('print("Hello, World!")')
            os.mkdir(os.path.join(tmpdir, 'subdir'))
            with open(python_file2_path, 'w') as f:
                f.write('print("Hello, Python!")')
            result = find_python_files(tmpdir)
            self.assertEqual(result, [python_file1_path, python_file2_path])

    def test_non_python_file(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            non_python_file_path = os.path.join(tmpdir, 'test.txt')
            with open(non_python_file_path, 'w') as f:
                f.write('This is a non-Python file.')
            result = find_python_files(tmpdir)
            self.assertEqual(result, [])

    def test_directory_with_subdirectories(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            subdir1_path = os.path.join(tmpdir, 'subdir1')
            subdir2_path = os.path.join(tmpdir, 'subdir1', 'subdir2')
            python_file1_path = os.path.join(tmpdir, 'subdir1', 'test1.py')
            python_file2_path = os.path.join(tmpdir, 'subdir1', 'subdir2', 'test2.py')
            python_file3_path = os.path.join(tmpdir, 'test3.py')
            os.mkdir(subdir1_path)
            os.mkdir(subdir2_path)
            with open(python_file1_path, 'w') as f:
                f.write('print("Hello, Subdir1!")')
            with open(python_file2_path, 'w') as f:
                f.write('print("Hello, Subdir2!")')
            with open(python_file3_path, 'w') as f:
                f.write('print("Hello, World!")')
            result = find_python_files(tmpdir)
            self.assertEqual(result, [python_file1_path, python_file2_path, python_file3_path])

if __name__ == '__main__':
    main()