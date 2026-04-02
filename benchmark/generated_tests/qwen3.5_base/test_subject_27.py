import unittest

class TestSeparateDataTypes(unittest.TestCase):
    """
    Test suite for the separate_data_types function.
    """
    
    def test_all_integers(self):
        """Test with all integers."""
        input_string = "1 2 3 4 5"
        int_list, float_list, str_list = separate_data_types(input_string)
        self.assertEqual(int_list, [1, 2, 3, 4, 5])
        self.assertEqual(float_list, [])
        self.assertEqual(str_list, [])
        
    def test_all_floats(self):
        """Test with all floats."""
        input_string = "1.5 2.5 3.5"
        int_list, float_list, str_list = separate_data_types(input_string)
        self.assertEqual(int_list, [])
        self.assertEqual(float_list, [1.5, 2.5, 3.5])
        self.assertEqual(str_list, [])
        
    def test_all_strings(self):
        """Test with all strings."""
        input_string = "hello world 123"
        int_list, float_list, str_list = separate_data_types(input_string)
        self.assertEqual(int_list, [])
        self.assertEqual(float_list, [])
        self.assertEqual(str_list, ["hello", "world", "123"])
        
    def test_mixed_types(self):
        """Test with mixed types."""
        input_string = "1 2.5 hello 3 4.0 world"
        int_list, float_list, str_list = separate_data_types(input_string)
        self.assertEqual(int_list, [1, 3])
        self.assertEqual(float_list, [2.5, 4.0])
        self.assertEqual(str_list, ["hello", "world"])
        
    def test_empty_string(self):
        """Test with an empty string."""
        input_string = ""
        int_list, float_list, str_list = separate_data_types(input_string)
        self.assertEqual(int_list, [])
        self.assertEqual(float_list, [])
        self.assertEqual(str_list, [])
        
    def test_single_value(self):
        """Test with a single value."""
        input_string = "1"
        int_list, float_list, str_list = separate_data_types(input_string)
        self.assertEqual(int_list, [1])
        self.assertEqual(float_list, [])
        self.assertEqual(str_list, [])
        
    def test_negative_numbers(self):
        """Test with negative numbers."""
        input_string = "-1 -2.5 -3"
        int_list, float_list, str_list = separate_data_types(input_string)
        self.assertEqual(int_list, [-1, -3])
        self.assertEqual(float_list, [-2.5])
        self.assertEqual(str_list, [])
        
    def test_special_characters(self):
        """Test with special characters."""
        input_string = "1 2.5 !@#$% 3 4.0"
        int_list, float_list, str_list = separate_data_types(input_string)
        self.assertEqual(int_list, [1, 3])
        self.assertEqual(float_list, [2.5, 4.0])
        self.assertEqual(str_list, ["!@#$%"])
        
    def test_whitespace_handling(self):
        """Test with extra whitespace."""
        input_string = "  1  2.5  3  4.0  "
        int_list, float_list, str_list = separate_data_types(input_string)
        self.assertEqual(int_list, [1, 3])
        self.assertEqual(float_list, [2.5, 4.0])
        self.assertEqual(str_list, [])
        
    def test_large_numbers(self):
        """Test with large numbers."""
        input_string = "1000000 2000000.5 3000000"
        int_list, float_list, str_list = separate_data_types(input_string)
        self.assertEqual(int_list, [1000000, 3000000])
        self.assertEqual(float_list, [2000000.5])
        self.assertEqual(str_list, [])
        
    def test_zero_values(self):
        """Test with zero values."""
        input_string = "0 0.0 0.00"
        int_list, float_list, str_list = separate_data_types(input_string)
        self.assertEqual(int_list, [0])
        self.assertEqual(float_list, [0.0, 0.00])
        self.assertEqual(str_list, [])
        
    def test_decimal_places(self):
        """Test with various decimal places."""
        input_string = "1.1 2.22 3.333 4.4444"
        int_list, float_list, str_list = separate_data_types(input_string)
        self.assertEqual(int_list, [])
        self.assertEqual(float_list, [1.1, 2.22, 3.333, 4.4444])
        self.assertEqual(str_list, [])
        
    def test_negative_floats(self):
        """Test with negative floats."""
        input_string = "-1.5 -2.5 -3.5"
        int_list, float_list, str_list = separate_data_types(input_string)
        self.assertEqual(int_list, [])
        self.assertEqual(float_list, [-1.5, -2.5, -3.5])
        self.assertEqual(str_list, [])
        
    def test_mixed_negative_positive(self):
        """Test with mixed negative and positive numbers."""
        input_string = "-1 2 -3.5 4.5"
        int_list, float_list, str_list = separate_data_types(input_string)
        self.assertEqual(int_list, [-1, 4])
        self.assertEqual(float_list, [-3.5, 4.5])
        self.assertEqual(str_list, [])
        
    def test_strings_with_numbers(self):
        """Test with strings that contain numbers."""
        input_string = "123 456 789"
        int_list, float_list, str_list = separate_data_types(input_string)
        self.assertEqual(int_list, [123, 456, 789])
        self.assertEqual(float_list, [])
        self.assertEqual(str_list, [])
        
    def test_strings_with_spaces(self):
        """Test with strings that contain spaces."""
        input_string = "hello world 123 456"
        int_list, float_list, str_list = separate_data_types(input_string)
        self.assertEqual(int_list, [123, 456])
        self.assertEqual(float_list, [])
        self.assertEqual(str_list, ["hello", "world"])
        
    def test_strings_with_special_characters(self):
        """Test with strings that contain special characters."""
        input_string = "hello! world? 123 456"
        int_list, float_list, str_list = separate_data