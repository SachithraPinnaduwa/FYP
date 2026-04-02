from subject_91 import *

import unittest

class TestReverseString(unittest.TestCase):
    def test_normal_case_with_typical_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")

    def test_normal_case_with_mixed_case_string(self):
        self.assertEqual(reverse_string("Python123"), "321nohtyP")

    def test_edge_case_with_empty_string(self):
        self.assertEqual(reverse_string(""), "")

    def test_edge_case_with_single_character_string(self):
        self.assertEqual(reverse_string("a"), "a")

    def test_error_handling_with_non_string_input(self):
        with self.assertRaises(TypeError):
            reverse_string(123)

if __name__ == '__main__':
    unittest.main()