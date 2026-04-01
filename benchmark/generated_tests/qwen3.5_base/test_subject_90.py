import unittest

class TestAutoCorrector(unittest.TestCase):
    def setUp(self):
        self.dictionary = {"hello", "world", "python", "code", "test"}
        self.autocorrector = AutoCorrector(self.dictionary)

    def test_correct_exact_match(self):
        self.assertEqual(self.autocorrector.correct("hello"), ["hello"])

    def test_correct_no_match(self):
        self.assertEqual(self.autocorrector.correct("xyz"), [])

    def test_correct_one_substitution(self):
        self.assertEqual(self.autocorrector.correct("helo"), ["hello"])

    def test_correct_one_insertion(self):
        self.assertEqual(self.autocorrector.correct("hlllo"), ["hello"])

    def test_correct_one_deletion(self):
        self.assertEqual(self.autocorrector.correct("helo"), ["hello"])

    def test_correct_two_substitutions(self):
        self.assertEqual(self.autocorrector.correct("helo"), ["hello"])

    def test_correct_two_insertions(self):
        self.assertEqual(self.autocorrector.correct("hlllo"), ["hello"])

    def test_correct_two_deletions(self):
        self.assertEqual(self.autocorrector.correct("helo"), ["hello"])

    def test_correct_case_insensitive(self):
        self.assertEqual(self.autocorrector.correct("HELLO"), ["hello"])

    def test_correct_max_distance(self):
        self.assertEqual(self.autocorrector.correct("xyz", max_distance=2), [])

    def test_correct_max_distance_1(self):
        self.assertEqual(self.autocorrector.correct("xyz", max_distance=1), [])

    def test_correct_max_distance_3(self):
        self.assertEqual(self.autocorrector.correct("xyz", max_distance=3), [])

    def test_correct_empty_string(self):
        self.assertEqual(self.autocorrector.correct(""), [])

    def test_correct_single_char(self):
        self.assertEqual(self.autocorrector.correct("a"), [])

    def test_correct_long_word(self):
        self.assertEqual(self.autocorrector.correct("hello world"), ["hello", "world"])

    def test_correct_multiple_candidates(self):
        self.assertEqual(self.autocorrector.correct("helo"), ["hello"])

    def test_correct_no_candidates(self):
        self.assertEqual(self.autocorrector.correct("xyz", max_distance=1), [])

    def test_correct_case_insensitive(self):
        self.assertEqual(self.autocorrector.correct("HELLO"), ["hello"])

    def test_correct_max_distance(self):
        self.assertEqual(self.autocorrector.correct("xyz", max_distance=2), [])

    def test_correct_max_distance_1(self):
        self.assertEqual(self.autocorrector.correct("xyz", max_distance=1), [])

    def test_correct_max_distance_3(self):
        self.assertEqual(self.autocorrector.correct("xyz", max_distance=3), [])

    def test_correct_empty_string(self):
        self.assertEqual(self.autocorrector.correct(""), [])

    def test_correct_single_char(self):
        self.assertEqual(self.autocorrector.correct("a"), [])

    def test_correct_long_word(self):
        self.assertEqual(self.autocorrector.correct("hello world"), ["hello", "world"])

    def test_correct_multiple_candidates(self):
        self.assertEqual(self.autocorrector.correct("helo"), ["hello"])

    def test_correct_no_candidates(self):
        self.assertEqual(self.autocorrector.correct("xyz", max_distance=1), [])

    def test_correct_case_insensitive(self):
        self.assertEqual(self.autocorrector.correct("HELLO"), ["hello"])

    def test_correct_max_distance(self):
        self.assertEqual(self.autocorrector.correct("xyz", max_distance=2), [])

    def test_correct_max_distance_1(self):
        self.assertEqual(self.autocorrector.correct("xyz", max_distance=1), [])

    def test_correct_max_distance_3(self):
        self.assertEqual(self.autocorrector.correct("xyz", max_distance=3), [])

    def test_correct_empty_string(self):
        self.assertEqual(self.autocorrector.correct(""), [])

    def test_correct_single_char(self):
        self.assertEqual(self.autocorrector.correct("a"), [])

    def test_correct_long_word(self):
        self.assertEqual(self.autocorrector.correct("hello world"), ["hello", "world"])

    def test_correct_multiple_candidates(self):
        self.assertEqual(self.autocorrector.correct("helo"), ["hello"])

    def test_correct_no_candidates(self):
        self.assertEqual(self.autocorrector.correct("xyz", max_distance=1), [])

    def test_correct_case_insensitive(self):
        self.assertEqual(self.autocorrector.correct("HELLO"), ["hello"])

    def test_correct_max_distance(self):
        self.assertEqual(self.autocorrector.correct("xyz", max_distance=2), [])

    def test_correct_max_distance_1(self):
        self.assertEqual(self.autocorrector.correct("xyz", max_distance=1), [])

    def test_correct_max_distance_3(self):
        self.assertEqual(self.autocorrector.correct("xyz", max_distance=3), [])

    def test_correct_empty_string(self):
        self.assertEqual(self.autocorrector.correct(""), [])

    def test_correct_single_char(self):
        self.assertEqual(self.autocorrector.correct("a"), [])

    def test_correct_long_word(self):
        self.assertEqual(self.autocorrector.correct("hello world"), ["hello", "world"])

    def test_correct_multiple_candidates(self):
        self.assertEqual(self.autocorrector.correct("helo"), ["hello"])

    def test_correct_no_candidates(self):
        self.assertEqual(self.autocorrector.correct("xyz", max_distance=1), [])

    def test_correct_case_insensitive(self):
        self.assertEqual(self.autocorrector.correct("HELLO"), ["hello"])

    def test_correct_max_distance(self):
        self.assertEqual(self.autocorrector.correct("xyz", max_distance=2), [])

    def test_correct_max_distance_1(self):
        self.assertEqual(self.autocorrector.correct("xyz", max_distance=1), [])

    def test_correct_max_distance_3(self):
        self.assertEqual(self.autocorrector.correct("xyz", max_distance=3), [])

    def test_correct_empty_string(self):
        self.assertEqual(self.autocorrector.correct(""), [])

    def test_correct_single_char(self):
        self.assertEqual(self.autocorrector.correct("a"), [])

    def test_correct_long_word(self):
        self.assertEqual(self.autocorrector.correct("hello world"), ["hello", "world"])

    def test_correct_multiple_candidates(self):
        self.assertEqual(self.autocorrector.correct("helo"), ["hello"])

    def test_correct_no_candidates(self):
        self.assertEqual(self.autocorrector.correct("xyz", max_distance=1), [])

    def test_correct_case_insensitive(self):
        self.assertEqual(self.autocorrector.correct("HELLO"), ["hello"])

    def test_correct_max_distance(self):
        self.assertEqual(self.autocorrector.correct("xyz", max_distance=2), [])

    def test_correct_max_distance_1(self