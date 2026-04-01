import unittest

class TestTextTokenizer(unittest.TestCase):
    def setUp(self):
        self.tokenizer = TextTokenizer(stop_words=['the', 'a', 'an', 'is', 'in'])

    def test_tokenize(self):
        text = "The quick brown fox jumps over the lazy dog."
        expected = ["quick", "brown", "fox", "jumps", "over", "lazy", "dog"]
        self.assertEqual(self.tokenizer.tokenize(text), expected)

    def test_tokenize_with_stop_words(self):
        text = "The quick brown fox jumps over the lazy dog."
        expected = ["quick", "brown", "fox", "jumps", "over", "lazy", "dog"]
        self.assertEqual(self.tokenizer.tokenize(text), expected)

    def test_tokenize_empty_string(self):
        self.assertEqual(self.tokenizer.tokenize(""), [])

    def test_tokenize_single_word(self):
        self.assertEqual(self.tokenizer.tokenize("hello"), ["hello"])

    def test_tokenize_multiple_words(self):
        text = "Hello world, this is a test."
        expected = ["hello", "world", "this", "test"]
        self.assertEqual(self.tokenizer.tokenize(text), expected)

    def test_tokenize_with_punctuation(self):
        text = "Hello, world! This is a test."
        expected = ["hello", "world", "this", "test"]
        self.assertEqual(self.tokenizer.tokenize(text), expected)

    def test_tokenize_with_numbers(self):
        text = "The price is 100 dollars."
        expected = ["price", "dollars"]
        self.assertEqual(self.tokenizer.tokenize(text), expected)

    def test_tokenize_with_special_characters(self):
        text = "Hello! @#$% World? ^&*() Test."
        expected = ["hello", "world", "test"]
        self.assertEqual(self.tokenizer.tokenize(text), expected)

    def test_tokenize_with_capital_letters(self):
        text = "Hello World! This Is A Test."
        expected = ["hello", "world", "this", "test"]
        self.assertEqual(self.tokenizer.tokenize(text), expected)

    def test_tokenize_with_newlines(self):
        text = "Hello\nWorld\nThis\nIs\nA\nTest."
        expected = ["hello", "world", "this", "is", "a", "test"]
        self.assertEqual(self.tokenizer.tokenize(text), expected)

    def test_tokenize_with_tabs(self):
        text = "Hello\tWorld\tThis\tIs\tA\tTest."
        expected = ["hello", "world", "this", "is", "a", "test"]
        self.assertEqual(self.tokenizer.tokenize(text), expected)

    def test_tokenize_with_multiple_spaces(self):
        text = "Hello   World   This   Is   A   Test."
        expected = ["hello", "world", "this", "is", "a", "test"]
        self.assertEqual(self.tokenizer.tokenize(text), expected)

    def test_tokenize_with_hyphens(self):
        text = "Hello-world! This-is-a-test."
        expected = ["hello", "world", "this", "is", "a", "test"]
        self.assertEqual(self.tokenizer.tokenize(text), expected)

    def test_tokenize_with_apostrophes(self):
        text = "It's a beautiful day! She's going to the store."
        expected = ["its", "beautiful", "day", "shes", "going", "store"]
        self.assertEqual(self.tokenizer.tokenize(text), expected)

    def test_tokenize_with_ellipsis(self):
        text = "Hello... World... This... Is... A... Test..."
        expected = ["hello", "world", "this", "is", "a", "test"]
        self.assertEqual(self.tokenizer.tokenize(text), expected)

    def test_tokenize_with_question_marks(self):
        text = "Hello? World? This? Is? A? Test?"
        expected = ["hello", "world", "this", "is", "a", "test"]
        self.assertEqual(self.tokenizer.tokenize(text), expected)

    def test_tokenize_with_exclamation_marks(self):
        text = "Hello! World! This! Is! A! Test!"
        expected = ["hello", "world", "this", "is", "a", "test"]
        self.assertEqual(self.tokenizer.tokenize(text), expected)

    def test_tokenize_with_colons(self):
        text = "Hello: World: This: Is: A: Test:"
        expected = ["hello", "world", "this", "is", "a", "test"]
        self.assertEqual(self.tokenizer.tokenize(text), expected)

    def test_tokenize_with_semicolons(self):
        text = "Hello; World; This; Is; A; Test;"
        expected = ["hello", "world", "this", "is", "a", "test"]
        self.assertEqual(self.tokenizer.tokenize(text), expected)

    def test_tokenize_with_commas(self):
        text = "Hello, World, This, Is, A, Test,"
        expected = ["hello", "world", "this", "is", "a", "test"]
        self.assertEqual(self.tokenizer.tokenize(text), expected)

    def test_tokenize_with_periods(self):
        text = "Hello. World. This. Is. A. Test."
        expected = ["hello", "world", "this", "is", "a", "test"]
        self.assertEqual(self.tokenizer.tokenize(text), expected)

    def test_tokenize_with_brackets(self):
        text = "Hello [World] This [Is] A [Test]."
        expected = ["hello", "world", "this", "is", "a", "test"]
        self.assertEqual(self.tokenizer.tokenize(text), expected)

    def test_tokenize_with_braces(self):
        text = "Hello {World} This {Is} A {Test}."
        expected = ["hello", "world", "this", "is", "a", "test"]
        self.assertEqual(self.tokenizer.tokenize(text), expected)

    def test_tokenize_with_parentheses(self):
        text = "Hello (World) This (Is) A (Test)."
        expected = ["hello", "world", "this", "is", "a", "test"]
        self.assertEqual(self.tokenizer.tokenize(text), expected)

    def test_tokenize_with_quotes(self):
        text = 'Hello "World" This "Is" A "Test".'
        expected = ["hello", "world", "this", "is", "a", "test"]
        self.assertEqual(self.tokenizer.tokenize(text), expected)

    def test_tokenize_with_single_quotes(self):
        text = "Hello 'World' This 'Is' A 'Test'."
        expected = ["hello", "world", "this", "is", "a", "test"]
        self.assertEqual(self.tokenizer.tokenize(text), expected)

    def test_tokenize_with_backslashes(self):
        text = "Hello \\World \\This \\Is \\A \\Test."
        expected = ["hello", "world",