import unittest
import os

class TestFindPythonFiles(unittest.TestCase):
    def test_find_python_files(self):
        # Test case 1: Empty directory
        directory_path = "test_directory"
        os.mkdir(directory_path)
        python_files = find_python_files(directory_path)
        self.assertEqual(python_files, [])

        # Test case 2: Non-empty directory
        os.mkdir(os.path.join(directory_path, "subdir"))
        with open(os.path.join(directory_path, "file1.py"), "w") as f:
            f.write("print('Hello, World!')")
        with open(os.path.join(directory_path, "subdir", "file2.py"), "w") as f:
            f.write("print('Hello, World!')")
        python_files = find_python_files(directory_path)
        self.assertEqual(python_files, [os.path.join(directory_path, "file1.py"), os.path.join(directory_path, "subdir", "file2.py")])

        # Test case 3: Non-Python files
        with open(os.path.join(directory_path, "file3.txt"), "w") as f:
            f.write("Hello, World!")
        python_files = find_python_files(directory_path)
        self.assertEqual(python_files, [os.path.join(directory_path, "file1.py"), os.path.join(directory_path, "subdir", "file2.py")])

        # Test case 4: Non-Python files in subdirectories
        with open(os.path.join(directory_path, "subdir", "file3.txt"), "w") as f:
            f.write("Hello, World!")
        python_files = find_python_files(directory_path)
        self.assertEqual(python_files, [os.path.join(directory_path, "file1.py"), os.path.join(directory_path, "subdir", "file2.py")])

        # Clean up test directory
        os.rmdir(directory_path)

if __name__ == "__main__":
    unittest.main()

### Explanation:

The