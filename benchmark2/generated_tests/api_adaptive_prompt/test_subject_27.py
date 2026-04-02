from subject_27 import *

import unittest

def separate_data_types(input_string):
    """
    Separate the input string of space-separated values into integers, floats, and strings.
    
    Parameters:
    input_string (str): A string of space-separated values.
    
    Returns:
    tuple: Three lists containing integers, floats, and strings respectively.
    """
    
    int_list = []
    float_list = []
    str_list = []
    
    # Split the input string into a list
    user_list = input_string.split()
    
    # For each item in the list, try to cast to each type
    for item in user_list:
        try:
            # Try to cast the item to int. If successful, add to int_list
            int_list.append(int(item))
        except ValueError:
            try:
                # If it can't be cast to int, try to cast to float. 
                # If successful, add to float_list
                float_list.append(float(item))
            except ValueError:
                # If it can't be cast to either numerical type, treat it as a string.
                # Add to str_list
                str_list.append(item)
                
    return int_list, float_list, str_list

class TestSeparateDataTypes(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual(separate_data_types("10 20.5 hello 30 40.7 world"), ([10, 30], [20.5, 40.7], ['hello', 'world']))
    
    def test_edge_case_empty_string(self):
        self.assertEqual(separate_data_types(""), ([], [], []))
    
    def test_edge_case_only_integers(self):
        self.assertEqual(separate_data_types("1 2 3 4 5"), ([1, 2, 3, 4, 5], [], []))
    
    def test_edge_case_only_floats(self):
        self.assertEqual(separate_data_types("1.1 2.2 3.3 4.4 5.5"), ([], [1.1, 2.2, 3.3, 4.4, 5.5], []))
    
    def test_edge_case_only_strings(self):
        self.assertEqual(separate_data_types("hello world test"), ([], [], ['hello', 'world', 'test']))
    
    def test_error_handling_non_numeric_characters(self):
        self.assertEqual(separate_data_types("abc def ghi"), ([], [], ['abc', 'def', 'ghi']))
    
    def test_error_handling_mixed_valid_and_invalid_values(self):
        self.assertEqual(separate_data_types("10 20.5 hello 30.1 40.7 world 50.2"), ([10], [20.5, 30.1, 40.7, 50.2], ['hello', 'world']))

if __name__ == '__main__':
    unittest.main()