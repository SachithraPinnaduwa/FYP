from subject_22 import *

import unittest
from typing import List
import os
from find_python_files import find_python_files

class TestFindPythonFiles(unittest.TestCase):
    def test_find_python_files(self):
        test_dir = "test_directory"
        os.makedirs(test_dir, exist_ok=True)
        os.makedirs(os.path.join(test_dir, "subdir"), exist_ok=True)
        with open(os.path.join(test_dir, "test.py"), "w") as f:
            f.write("print('Hello, World!')")
        with open(os.path.join(test_dir, "test.txt"), "w") as f:
            f.write("This is a test file.")
        with open(os.path.join(test_dir, "subdir", "test2.py"), "w") as f:
            f.write("print('Hello, Subdir!')")

        expected_output = [
            os.path.join(test_dir, "test.py"),
            os.path.join(test_dir, "subdir", "test2.py")
        ]

        self.assertEqual(sorted(find_python_files(test_dir)), sorted(expected_output))

        os.remove(os.path.join(test_dir, "test.py"))
        os.remove(os.path.join(test_dir, "test.txt"))
        os.remove(os.path.join(test_dir, "subdir", "test2.py"))
        os.rmdir(os.path.join(test_dir, "subdir"))
        os.rmdir(test_dir)

if __name__ == '__main__':
    unittest.main()