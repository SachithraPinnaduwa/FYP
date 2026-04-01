import os
import tempfile
import unittest

class TestFindPythonFiles(unittest.TestCase):
    def test_no_python_files(self):
        # Create a temporary directory with no Python files
        with tempfile.TemporaryDirectory() as temp_dir:
            # Call the function and check that it returns an empty list
            self.assertEqual(find_python_files(temp_dir), [])

    def test_one_python_file(self):
        # Create a temporary directory with one Python file
        with tempfile.TemporaryDirectory() as temp_dir:
            python_file = os.path.join(temp_dir, 'test.py')
            with open(python_file, 'w') as f:
                f.write('print("Hello, world!")')
            # Call the function and check that it returns a list containing the path to the Python file
            self.assertEqual(find_python_files(temp_dir), [python_file])

    def test_multiple_python_files(self):
        # Create a temporary directory with multiple Python files
        with tempfile.TemporaryDirectory() as temp_dir:
            python_file1 = os.path.join(temp_dir, 'test1.py')
            with open(python_file1, 'w') as f:
                f.write('print("Hello, world!")')
            python_file2 = os.path.join(temp_dir, 'test2.py')
            with open(python_file2, 'w') as f:
                f.write('print("Hello, Python!")')
            # Call the function and check that it returns a list containing the paths to the Python files
            self.assertEqual(find_python_files(temp_dir), [python_file1, python_file2])

    def test_python_files_in_subdirectory(self):
        # Create a temporary directory with a Python file in a subdirectory
        with tempfile.TemporaryDirectory() as temp_dir:
            subdirectory = os.path.join(temp_dir, 'subdir')
            os.mkdir(subdirectory)
            python_file = os.path.join(subdirectory, 'test.py')
            with open(python_file, 'w') as f:
                f.write('print("Hello, world!")')
            # Call the function and check that it returns a list containing the path to the Python file
            self.assertEqual(find_python_files(temp_dir), [python_file])

    def test_non_python_files(self):
        # Create a temporary directory with non-Python files
        with tempfile.TemporaryDirectory() as temp_dir:
            non_python_file = os.path.join(temp_dir, 'test.txt')
            with open(non_python_file, 'w') as f:
                f.write('Hello, world!')
            # Call the function and check that it returns an empty list
            self.assertEqual(find_python_files(temp_dir), [])

    def test_empty_directory(self):
        # Call the function on an empty directory
        with tempfile.TemporaryDirectory() as temp_dir:
            # Call the function and check that it returns an empty list
            self.assertEqual(find_python_files(temp_dir), [])

if __name__ == '__main__':
    pass