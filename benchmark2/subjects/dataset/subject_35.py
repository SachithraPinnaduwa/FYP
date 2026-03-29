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