import unittest

class TestSeparateDataTypes(unittest.TestCase):

    def test_empty_input(self):
        self.assertEqual(separate_data_types(""), ([], [], []))

    def test_all_integers(self):
        self.assertEqual(separate_data_types("1 2 3"), ([1, 2, 3], [], []))

    def test_all_floats(self):
        self.assertEqual(separate_data_types("1.5 2.5 3.5"), ([], [1.5, 2.5, 3.5], []))

    def test_mixed_integers_and_floats(self):
        self.assertEqual(separate_data_types("1 2.5 3"), ([1, 3], [2.5], []))

    def test_mixed_values(self):
        self.assertEqual(separate_data_types("1 2.5 abc"), ([1], [2.5], ['abc']))

    def test_non_numeric_strings(self):
        self.assertEqual(separate_data_types("abc def ghi"), ([], [], ['abc', 'def', 'ghi']))

    def test_leading_trailing_spaces(self):
        self.assertEqual(separate_data_types(" 1 2.5 abc "), ([1], [2.5], ['abc']))

    def test_special_characters(self):
        self.assertEqual(separate_data_types("1,2.5;abc"), ([1], [2.5], ['abc']))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            separate_data_types(123)

if __name__ == '__main__':
    unittest.main()