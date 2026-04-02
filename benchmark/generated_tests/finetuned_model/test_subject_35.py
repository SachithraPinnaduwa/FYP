import unittest

def get_most_frequent_words(string, stop_words, min_word_length, num_words):
    string = string.lower()
    string = re.sub(r'[^\w\s]', '', string)
    words = string.split()
    words = [word for word in words if word not in stop_words and len(word) >= min_word_length]
    word_counts = Counter(words)
    most_frequent_words = word_counts.most_common(num_words)
    return most_frequent_words

class TestGetMostFrequentWords(unittest.TestCase):
    def test_get_most_frequent_words(self):
        self.assertEqual(get_most_frequent_words('Hello world hello', ['hello'], 3, 1), [('world', 1)])
        self.assertEqual(get_most_frequent_words('The quick brown fox jumps over the lazy dog', ['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'lazy'], 3, 1), [('dog', 1)])
        self.assertEqual(get_most_frequent_words('Lorem ipsum dolor sit amet, consectetur adipiscing elit', ['lorem', 'ipsum'], 4, 2), [('dolor', 1), ('sit', 1)])
        self.assertEqual(get_most_frequent_words('One apple and two oranges, one apple', ['and'], 4, 2), [('one', 2), ('apples', 1)])
        self.assertEqual(get_most_frequent_words('Python is an interpreted, high-level and general-purpose programming language', ['is', 'an', 'and', 'a'], 4, 3), [('python', 1), ('interpreted', 1), ('highlevel', 1)])
        self.assertEqual(get_most_frequent_words('Every moment is a fresh beginning', ['every', 'moment'], 4, 2), [('is', 1), ('a', 1)])

if __name__ == '__main__':
    unittest.main()