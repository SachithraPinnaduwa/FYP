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
    def test_separate_data_types(self):
        self.assertEqual(separate_data_types("1 2 3"), ([1, 2, 3], [], []))
        self.assertEqual(separate_data_types("1.1 2.2 3.3"), ([], [1.1, 2.2, 3.3], []))
        self.assertEqual(separate_data_types("1 2.2 abc"), ([1], [2.2], ['abc']))
        self.assertEqual(separate_data_types("abc 1.1 2"), ([], [1.1], ['abc', '2']))
        self.assertEqual(separate_data_types("abc def ghi"), ([], [], ['abc', 'def', 'ghi']))
        self.assertEqual(separate_data_types("1.1 abc 2"), ([1], [2.0], ['abc']))
        self.assertEqual(separate_data_types("1 abc 2.2"), ([1], [2.2], ['abc']))
        self.assertEqual(separate_data_types("abc 1 2.2"), ([1], [2.2], ['abc']))
        self.assertEqual(separate_data_types("1.1 abc 2.2"), ([], [1.1, 2.2], ['abc']))
        self.assertEqual(separate_data_types("abc 1.1 2.2"), ([], [1.1, 2.2], ['abc']))
        self.assertEqual(separate_data_types("1 2.2 abc 3.3"), ([1], [2.2, 3.3], ['abc']))
        self.assertEqual(separate_data_types("abc 1 2.2 3.3"), ([1], [2.2, 3.3], ['abc']))
        self.assertEqual(separate_data_types("1.1 abc 2.2 3.3"), ([], [1.1, 2.2, 3.3], ['abc']))
        self.assertEqual(separate_data_types("abc 1.1 2.2 3.3"), ([], [1.1, 2.2, 3.3], ['abc']))
        self.assertEqual(separate_data_types("1 2.2 abc 3.3 4"), ([1], [2.2, 3.3, 4], ['abc']))
        self.assertEqual(separate_data_types("abc 1 2.2 3.3 4"), ([1], [2.2, 3.3, 4], ['abc']))
        self.assertEqual(separate_data_types("1.1 abc 2.2 3.3 4"), ([], [1.1, 2.2, 3.3, 4], ['abc']))
        self.assertEqual(separate_data_types("abc 1.1 2.2 3.3 4"), ([], [1.1, 2.2, 3.3, 4], ['abc']))
        self.assertEqual(separate_data_types("1 2.2 abc 3.3 4.4"), ([1], [2.2, 3.3, 4.4], ['abc']))
        self.assertEqual(separate_data_types("abc 1 2.2 3.3 4.4"), ([1], [2.2, 3.3, 4.4], ['abc']))
        self.assertEqual(separate_data_types("1.1 abc 2.2 3.3 4.4"), ([], [1.1, 2.2, 3.3, 4.4], ['abc']))
        self.assertEqual(separate_data_types