import unittest

class TestFindPythonFiles(unittest.TestCase):
    def test_find_python_files(self):
        # Test with a directory containing Python files
        test_directory = "test_directory"
        os.makedirs(test_directory, exist_ok=True)
        
        # Create some Python files
        with open(os.path.join(test_directory, "test_file1.py"), "w") as f:
            f.write("print('Hello, World!')")
        
        with open(os.path.join(test_directory, "test_file2.py"), "w") as f:
            f.write("print('Hello, World!')")
        
        # Create a subdirectory with Python files
        sub_directory = os.path.join(test_directory, "sub_directory")
        os.makedirs(sub_directory, exist_ok=True)
        
        with open(os.path.join(sub_directory, "test_file3.py"), "w") as f:
            f.write("print('Hello, World!')")
        
        # Test the function
        result = find_python_files(test_directory)
        
        # Check if the function returns the expected list of Python files
        self.assertEqual(len(result), 3)
        self.assertIn(os.path.join(test_directory, "test_file1.py"), result)
        self.assertIn(os.path.join(test_directory, "test_file2.py"), result)
        self.assertIn(os.path.join(sub_directory, "test_file3.py"), result)
        
        # Clean up
        import shutil
        shutil.rmtree(test_directory)

if __name__ == '__main__':
    unittest.main()
