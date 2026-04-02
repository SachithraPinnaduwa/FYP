import unittest

class TestGetMostFrequentWords(unittest.TestCase):
    def test_get_most_frequent_words(self):
        # Test case 1
        string = "Hello, world! Hello, world! Hello, world!"
        stop_words = ["the", "a", "an"]
        min_word_length = 3
        num_words = 3
        expected = [("hello", 3), ("world", 3)]
        self.assertEqual(get_most_frequent_words(string, stop_words, min_word_length, num_words), expected)

        # Test case 2
        string = "The quick brown fox jumps over the lazy dog."
        stop_words = ["the", "a", "an"]
        min_word_length = 3
        num_words = 3
        expected = [("quick", 1), ("brown", 1), ("fox", 1)]
        self.assertEqual(get_most_frequent_words(string, stop_words, min_word_length, num_words), expected)

        # Test case 3
        string = "Python is a great programming language. Python is a great programming language."
        stop_words = ["the", "a", "an"]
        min_word_length = 3
        num_words = 3
        expected = [("python", 2), ("great", 2), ("programming", 2)]
        self.assertEqual(get_most_frequent_words(string, stop_words, min_word_length, num_words), expected)

        # Test case 4
        string = "The quick brown fox jumps over the lazy dog."
        stop_words = ["the", "a", "an"]
        min_word_length = 3
        num_words = 1
        expected = [("quick", 1)]
        self.assertEqual(get_most_frequent_words(string, stop_words, min_word_length, num_words), expected)

        # Test case 5
        string = "The quick brown fox jumps over the lazy dog."
        stop_words = ["the", "a", "an"]
        min_word_length = 3
        num_words = 0
        expected = []
        self.assertEqual(get_most_frequent_words(string, stop_words, min_word_length, num_words), expected)

if __name__ == '__main__':
    unittest.main()
