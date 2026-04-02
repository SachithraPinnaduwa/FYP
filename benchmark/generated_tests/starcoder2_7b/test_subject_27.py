import unittest

class TestSeparateDataTypes(unittest.TestCase):
    def test_separate_data_types(self):
        # Test case 1: Input is a string of space-separated integers
        input_string = "1 2 3 4 5"
        expected_int_list = [1, 2, 3, 4, 5]
        expected_float_list = []
        expected_str_list = []
        int_list, float_list, str_list = separate_data_types(input_string)
        self.assertEqual(int_list, expected_int_list)
        self.assertEqual(float_list, expected_float_list)
        self.assertEqual(str_list, expected_str_list)

        # Test case 2: Input is a string of space-separated floats
        input_string = "1.1 2.2 3.3 4.4 5.5"
        expected_int_list = []
        expected_float_list = [1.1, 2.2, 3.3, 4.4, 5.5]
        expected_str_list = []
        int_list, float_list, str_list = separate_data_types(input_string)
        self.assertEqual(int_list, expected_int_list)
        self.assertEqual(float_list, expected_float_list)
        self.assertEqual(str_list, expected_str_list)

        # Test case 3: Input is a string of space-separated strings
        input_string = "a b c d e"
        expected_int_list = []
        expected_float_list = []
        expected_str_list = ["a", "b", "c", "d", "e"]
        int_list, float_list, str_list = separate_data_types(input_string)
        self.assertEqual(int_list, expected_int_list)
        self.assertEqual(float_list, expected_float_list)
        self.assertEqual(str_list, expected_str_list)

        # Test case 4: Input is a string of space-separated integers, floats, and strings
        input_string = "1 2.2 3.3 4.4 5.5 a b c d e"
        expected_int_