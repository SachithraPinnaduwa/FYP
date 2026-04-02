from subject_63 import *

import unittest

class TestEntranceFunction(unittest.TestCase):
    def test_normal_case_n_greater_than_1(self):
        self.assertEqual(entrance(5), 5)

    def test_normal_case_n_is_1(self):
        self.assertEqual(entrance(1), 1)

    def test_normal_case_n_is_0(self):
        self.assertEqual(entrance(0), 0)

    def test_edge_case_negative_integer(self):
        self.assertEqual(entrance(-5), 0)

    def test_edge_case_n_is_0(self):
        self.assertEqual(entrance(0), 0)

    def test_error_handling_non_integer_input(self):
        with self.assertRaises(TypeError):
            entrance('5')

if __name__ == '__main__':
    unittest.main()