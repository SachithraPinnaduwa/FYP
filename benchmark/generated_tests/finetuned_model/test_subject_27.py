import unittest

class TestSeparateDataTypes(unittest.TestCase):
    
    def test_separate_integers(self):
        # Test case with only integers
        input_string = "1 2 3 4 5"
        expected_output = ([1, 2, 3, 4, 5], [], [])
        self.assertEqual(separate_data_types(input_string), expected_output)
        
    def test_separate_floats(self):
        # Test case with only floats
        input_string = "1.1 2.2 3.3 4.4 5.5"
        expected_output = ([], [1.1, 2.2, 3.3, 4.4, 5.5], [])
        self.assertEqual(separate_data_types(input_string), expected_output)
        
    def test_separate_strings(self):
        # Test case with only strings
        input_string = "abc def ghi jkl mno"
        expected_output = ([], [], ['abc', 'def', 'ghi', 'jkl', 'mno'])
        self.assertEqual(separate_data_types(input_string), expected_output)
        
    def test_separate_integers_and_strings(self):
        # Test case with integers and strings
        input_string = "1 2 3 abc def"
        expected_output = ([1, 2, 3], [], ['abc', 'def'])
        self.assertEqual(separate_data_types(input_string), expected_output)
        
    def test_separate_floats_and_strings(self):
        # Test case with floats and strings
        input_string = "1.1 2.2 3.3 abc def"
        expected_output = ([], [1.1, 2.2, 3.3], ['abc', 'def'])
        self.assertEqual(separate_data_types(input_string), expected_output)
        
    def test_separate_integers_floats_and_strings(self):
        # Test case with integers, floats, and strings
        input_string = "1 2 3 1.1 2.2 abc def"
        expected_output = ([1, 2, 3], [1.1, 2.2], ['abc', 'def'])
        self.assertEqual(separate_data_types(input_string), expected_output)
        
    def test_empty_input(self):
        # Test case with empty input
        input_string = ""
        expected_output = ([], [], [])
        self.assertEqual(separate_data_types(input_string), expected_output)
        
    def test_input_with_no_convertible_values(self):
        # Test case with no convertible values
        input_string = "abc def ghi"
        expected_output = ([], [], ['abc', 'def', 'ghi'])
        self.assertEqual(separate_data_types(input_string), expected_output)
        
    def test_input_with_mixed_types(self):
        # Test case with mixed types
        input_string = "1 2.2 abc 3.3 def"
        expected_output = ([1], [2.2, 3.3], ['abc', 'def'])
        self.assertEqual(separate_data_types(input_string), expected_output)