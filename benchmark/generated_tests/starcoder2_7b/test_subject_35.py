### Instruction:
Write a comprehensive Python unit test suite for the provided code.

### Input:
Problem Description:
Write a function named `get_most_frequent_words` that takes four parameters: a string, a list of stop words, a minimum word length, and the number of words to return. The function should return the specified number of most frequent words in the string, excluding the stop words and words that are less than the minimum word length. The function should handle cases and punctuation marks properly.

Code to Test:
import re
from collections import Counter

def get_most_frequent_words(string, stop_words, min_word_length, num_words):
    string = string.lower()
    string = re.sub(r'[^\w\s]', '', string)
    words = string.split()
    words = [word for word in words if word not in stop_words and len(word) >= min_word_length]
    word_counts = Counter(words)
    most_frequent_words = word_counts.most_common(num_words)
    return most_frequent_words