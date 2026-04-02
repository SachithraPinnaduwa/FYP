import unittest

class TestFilterStrings(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(filter_strings([], 3), [])

    def test_all_strings_short(self):
        self.assertEqual(filter_strings(["hi", "hello"], 3), [])

    def test_all_strings_long(self):
        self.assertEqual(filter_strings(["hello", "world"], 3), ["hello", "world"])

    def test_mixed_strings(self):
        self.assertEqual(filter_strings(["hi", "hello", "world"], 3), ["hello", "world"])

    def test_no_uppercase(self):
        self.assertEqual(filter_strings(["hello", "world"], 3), [])

    def test_with_uppercase(self):
        self.assertEqual(filter_strings(["hello", "WORLD"], 3), ["hello", "WORLD"])

    def test_single_character(self):
        self.assertEqual(filter_strings(["a"], 3), [])

    def test_multiple_uppercase(self):
        self.assertEqual(filter_strings(["HELLO", "WORLD"], 3), ["HELLO", "WORLD"])

    def test_mixed_case(self):
        self.assertEqual(filter_strings(["Hello", "WORLD"], 3), ["Hello", "WORLD"])

    def test_special_characters(self):
        self.assertEqual(filter_strings(["hello!", "world?"], 3), ["hello!", "world?"])

    def test_unicode_characters(self):
        self.assertEqual(filter_strings(["héllo", "wörld"], 3), ["héllo", "wörld"])

    def test_empty_string(self):
        self.assertEqual(filter_strings([""], 3), [])

    def test_whitespace_only(self):
        self.assertEqual(filter_strings(["   "], 3), [])

    def test_newline_character(self):
        self.assertEqual(filter_strings(["hello\n"], 3), ["hello\n"])

    def test_tab_character(self):
        self.assertEqual(filter_strings(["hello\t"], 3), ["hello\t"])

    def test_multiple_newlines(self):
        self.assertEqual(filter_strings(["hello\n\n"], 3), ["hello\n\n"])

    def test_multiple_tabs(self):
        self.assertEqual(filter_strings(["hello\t\t"], 3), ["hello\t\t"])

    def test_mixed_newlines_and_tabs(self):
        self.assertEqual(filter_strings(["hello\n\t"], 3), ["hello\n\t"])

    def test_mixed_uppercase_and_lowercase(self):
        self.assertEqual(filter_strings(["Hello", "WORLD"], 3), ["Hello", "WORLD"])

    def test_mixed_uppercase_and_special_characters(self):
        self.assertEqual(filter_strings(["Hello!", "WORLD?"], 3), ["Hello!", "WORLD?"])

    def test_mixed_uppercase_and_unicode_characters(self):
        self.assertEqual(filter_strings(["Héllo", "Wörld"], 3), ["Héllo", "Wörld"])

    def test_mixed_uppercase_and_whitespace(self):
        self.assertEqual(filter_strings(["Hello  ", "WORLD  "], 3), ["Hello  ", "WORLD  "])

    def test_mixed_uppercase_and_newlines(self):
        self.assertEqual(filter_strings(["Hello\n", "WORLD\n"], 3), ["Hello\n", "WORLD\n"])

    def test_mixed_uppercase_and_tabs(self):
        self.assertEqual(filter_strings(["Hello\t", "WORLD\t"], 3), ["Hello\t", "WORLD\t"])

    def test_mixed_uppercase_and_special_characters_and_unicode(self):
        self.assertEqual(filter_strings(["Hello!", "WORLD?"], 3), ["Hello!", "WORLD?"])

    def test_mixed_uppercase_and_whitespace_and_newlines(self):
        self.assertEqual(filter_strings(["Hello  \n", "WORLD  \n"], 3), ["Hello  \n", "WORLD  \n"])

    def test_mixed_uppercase_and_whitespace_and_tabs(self):
        self.assertEqual(filter_strings(["Hello  \t", "WORLD  \t"], 3), ["Hello  \t", "WORLD  \t"])

    def test_mixed_uppercase_and_special_characters_and_whitespace(self):
        self.assertEqual(filter_strings(["Hello!  ", "WORLD?  "], 3), ["Hello!  ", "WORLD?  "])

    def test_mixed_uppercase_and_special_characters_and_newlines(self):
        self.assertEqual(filter_strings(["Hello!\n", "WORLD?\n"], 3), ["Hello!\n", "WORLD?\n"])

    def test_mixed_uppercase_and_special_characters_and_tabs(self):
        self.assertEqual(filter_strings(["Hello!\t", "WORLD?\t"], 3), ["Hello!\t", "WORLD?\t"])

    def test_mixed_uppercase_and_unicode_and_whitespace(self):
        self.assertEqual(filter_strings(["Héllo  ", "Wörld  "], 3), ["Héllo  ", "Wörld  "])

    def test_mixed_uppercase_and_unicode_and_newlines(self):
        self.assertEqual(filter_strings(["Héllo\n", "Wörld\n"], 3), ["Héllo\n", "Wörld\n"])

    def test_mixed_uppercase_and_unicode_and_tabs(self):
        self.assertEqual(filter_strings(["Héllo\t", "Wörld\t"], 3), ["Héllo\t", "Wörld\t"])

    def test_mixed_uppercase_and_unicode_and_special_characters(self):
        self.assertEqual(filter_strings(["Héllo!", "Wörld?"], 3), ["Héllo!", "Wörld?"])

    def test_mixed_uppercase_and_unicode_and_whitespace_and_newlines(self):
        self.assertEqual(filter_strings(["Héllo  \n", "Wörld  \n"], 3), ["Héllo  \n", "Wörld  \n"])

    def test_mixed_uppercase_and_unicode_and_whitespace_and_tabs(self):
        self.assertEqual(filter_strings(["Héllo  \t", "Wörld  \t"], 3), ["Héllo  \t", "Wörld  \t"])

    def test_mixed_uppercase_and_unicode_and_special_characters_and_whitespace(self):
        self.assertEqual(filter_strings(["Héllo!  ", "Wörld?  "], 3), ["Héllo!  ", "Wörld?  "])

    def test_mixed_uppercase_and_unicode_and_special_characters_and_newlines(self):
        self.assertEqual(filter_strings(["Héllo!\n", "Wörld?\n"], 3), ["Héllo!\n", "Wörld?\n"])

    def test_mixed_uppercase_and_unicode_and_special_characters_and_tabs(self):
        self.assertEqual(filter_strings(["Héllo!\t", "Wörld?\t"], 3), ["Héllo!\t", "Wörld?\t"])

    def test_mixed_uppercase_and_unicode_and_whitespace_and_special_characters(self):
        self.assertEqual(filter_strings(["Héllo  !", "Wörld?  "], 3), ["Héllo