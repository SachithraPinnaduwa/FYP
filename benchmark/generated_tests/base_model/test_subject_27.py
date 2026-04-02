import unittest

class TestSeparateDataTypes(unittest.TestCase):

    def test_separate_data_types_with_integers(self):
        result = separate_data_types("1 2 3")
        self.assertEqual(result, ([1, 2, 3], [], []))

    def test_separate_data_types_with_floats(self):
        result = separate_data_types("1.0 2.5 3.75")
        self.assertEqual(result, ([], [1.0, 2.5, 3.75], []))

    def test_separate_data_types_with_strings(self):
        result = separate_data_types("one two three")
        self.assertEqual(result, ([], [], ['one', 'two', 'three']))

    def test_separate_data_types_mixed_types(self):
        result = separate_data_types("1 2.5 one")
        self.assertEqual(result, ([1], [2.5], ['one']))

    def test_separate_data_types_empty_string(self):
        result = separate_data_types("")
        self.assertEqual(result, ([], [], []))

    def test_separate_data_types_non_space_delimited(self):
        result = separate_data_types("1,2,3")
        self.assertEqual(result, ([1], [2.0], ['3']))

    def test_separate_data_types_invalid_input(self):
        result = separate_data_types("a b c d e f g")
        self.assertEqual(result, ([], [], ['a', 'b', 'c', 'd', 'e', 'f', 'g']))

if __name__ == '__main__':
    unittest.main()