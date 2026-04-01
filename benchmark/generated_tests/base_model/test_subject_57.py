import unittest

class TestFilterStrings(unittest.TestCase):

    def test_filter_strings_empty_list(self):
        self.assertEqual(filter_strings([], 3), [])

    def test_filter_strings_no_uppercase(self):
        self.assertEqual(filter_strings(["apple", "banana", "cherry"], 5), ["banana", "cherry"])

    def test_filter_strings_all_lowercase(self):
        self.assertEqual(filter_strings(["apple", "banana", "cherry"], 2), ["apple", "banana", "cherry"])

    def test_filter_strings_mixed_case(self):
        self.assertEqual(filter_strings(["Apple", "banana", "Cherry", "date"], 4), ["Apple", "Cherry"])

    def test_filter_strings_single_char(self):
        self.assertEqual(filter_strings(["A", "B", "C", "D"], 0), ["A", "B", "C", "D"])

    def test_filter_strings_long_string(self):
        self.assertEqual(filter_strings(["ThisIsAVeryLongString", "short", "AnotherOne"], 10), ["ThisIsAVeryLongString"])

    def test_filter_strings_multiple_conditions(self):
        self.assertEqual(filter_strings(["aBcDeF", "gHiJkL", "mNoPqR", "sTuVwXyZ"], 2), ["aBcDeF", "gHiJkL", "mNoPqR", "sTuVwXyZ"])

if __name__ == '__main__':
    unittest.main()