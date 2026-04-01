import unittest

class TestAutocompleteSystem(unittest.TestCase):
    def setUp(self):
        self.system = AutocompleteSystem(["i", "love", "leetcode", "code"], [1, 3, 2, 3])

    def test_initial_state(self):
        self.assertEqual(self.system.search_term, "")
        self.assertEqual(self.system.curr, self.system.root)

    def test_input_letter(self):
        result = self.system.input("l")
        self.assertEqual(result, ["leetcode", "love"])
        self.assertEqual(self.system.search_term, "l")

    def test_input_backspace(self):
        result = self.system.input("#")
        self.assertEqual(result, [])
        self.assertEqual(self.system.search_term, "")

    def test_input_multiple_letters(self):
        result = self.system.input("o")
        self.assertEqual(result, ["love"])
        self.assertEqual(self.system.search_term, "lo")

    def test_input_nonexistent_letter(self):
        result = self.system.input("z")
        self.assertEqual(result, [])
        self.assertEqual(self.system.search_term, "lz")

    def test_input_complete_sentence(self):
        result = self.system.input("e")
        self.assertEqual(result, ["leetcode"])
        self.assertEqual(self.system.search_term, "love")

    def test_input_multiple_sentences(self):
        result = self.system.input("e")
        self.assertEqual(result, ["leetcode"])
        self.assertEqual(self.system.search_term, "love")
        result = self.system.input("e")
        self.assertEqual(result, ["leetcode"])
        self.assertEqual(self.system.search_term, "love")

    def test_input_with_empty_prefix(self):
        result = self.system.input("a")
        self.assertEqual(result, [])
        self.assertEqual(self.system.search_term, "a")

    def test_input_with_long_prefix(self):
        result = self.system.input("l")
        self.assertEqual(result, ["leetcode", "love"])
        self.assertEqual(self.system.search_term, "l")
        result = self.system.input("o")
        self.assertEqual(result, ["love"])
        self.assertEqual(self.system.search_term, "lo")

    def test_input_with_special_characters(self):
        result = self.system.input("!")
        self.assertEqual(result, [])
        self.assertEqual(self.system.search_term, "!")

    def test_input_with_numbers(self):
        result = self.system.input("1")
        self.assertEqual(result, [])
        self.assertEqual(self.system.search_term, "1")

    def test_input_with_unicode(self):
        result = self.system.input("é")
        self.assertEqual(result, [])
        self.assertEqual(self.system.search_term, "é")

    def test_input_with_whitespace(self):
        result = self.system.input(" ")
        self.assertEqual(result, [])
        self.assertEqual(self.system.search_term, " ")

    def test_input_with_newline(self):
        result = self.system.input("\n")
        self.assertEqual(result, [])
        self.assertEqual(self.system.search_term, "\n")

    def test_input_with_tab(self):
        result = self.system.input("\t")
        self.assertEqual(result, [])
        self.assertEqual(self.system.search_term, "\t")

    def test_input_with_carriage_return(self):
        result = self.system.input("\r")
        self.assertEqual(result, [])
        self.assertEqual(self.system.search_term, "\r")

    def test_input_with_form_feed(self):
        result = self.system.input("\f")
        self.assertEqual(result, [])
        self.assertEqual(self.system.search_term, "\f")

    def test_input_with_vertical_tab(self):
        result = self.system.input("\v")
        self.assertEqual(result, [])
        self.assertEqual(self.system.search_term, "\v")

    def test_input_with_null(self):
        result = self.system.input("\0")
        self.assertEqual(result, [])
        self.assertEqual(self.system.search_term, "\0")

    def test_input_with_null_byte(self):
        result = self.system.input("\x00")
        self.assertEqual(result, [])
        self.assertEqual(self.system.search_term, "\x00")

    def test_input_with_null character(self):
        result = self.system.input("\u0000")
        self.assertEqual(result, [])
        self.assertEqual(self.system.search_term, "\u0000")

    def test_input_with_null character (2):
        result = self.system.input("\u0001")
        self.assertEqual(result, [])
        self.assertEqual(self.system.search_term, "\u0001")

    def test_input_with_null character (3):
        result = self.system.input("\u0002")
        self.assertEqual(result, [])
        self.assertEqual(self.system.search_term, "\u0002")

    def test_input_with_null character (4):
        result = self.system.input("\u0003")
        self.assertEqual(result, [])
        self.assertEqual(self.system.search_term, "\u0003")

    def test_input_with_null character (5):
        result = self.system.input("\u0004")
        self.assertEqual(result, [])
        self.assertEqual(self.system.search_term, "\u0004")

    def test_input_with_null character (6):
        result = self.system.input("\u0005")
        self.assertEqual(result, [])
        self.assertEqual(self.system.search_term, "\u0005")

    def test_input_with_null character (7):
        result = self.system.input("\u0006")
        self.assertEqual(result, [])
        self.assertEqual(self.system.search_term, "\u0006")

    def test_input_with_null character (8):
        result = self.system.input("\u0007")
        self.assertEqual(result, [])
        self.assertEqual(self.system.search_term, "\u0007")

    def test_input_with_null character (9):
        result = self.system.input("\u0008")
        self.assertEqual(result, [])
        self.assertEqual(self.system.search_term, "\u0008")

    def test_input_with_null character (10):
        result = self.system.input("\u0009")
        self.assertEqual(result, [])
        self.assertEqual(self.system.search_term, "\u0009")

    def test_input_with_null character (11):
        result = self.system.input("\u000a")
        self.assertEqual(result, [])
        self.assertEqual(self.system.search_term, "\u000a")

    def test_input_with_null character (12):
        result = self.system.input("\u000b")
        self.assertEqual(result, [])
        self.assertEqual(self.system.search_term, "\u000b")

    def test_input_with_null character (13):
        result = self.system.input("\u000c")
        self.assertEqual(result, [])
        self.assertEqual(self.system.search_term, "\u000c")

    def test_input_with_null character (14):
        result = self.system.input("\u000d")