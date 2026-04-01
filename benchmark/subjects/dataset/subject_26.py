import re
from typing import List

class TextTokenizer:
    def __init__(self, stop_words: List[str] = None):
        self.stop_words = set(stop_words or [])
        self.word_pattern = re.compile(r'\b\w+\b')

    def tokenize(self, text: str) -> List[str]:
        words = self.word_pattern.findall(text.lower())
        return [w for w in words if w not in self.stop_words]

    def get_ngrams(self, text: str, n: int) -> List[str]:
        tokens = self.tokenize(text)
        if len(tokens) < n:
            return []
        return [' '.join(tokens[i:i+n]) for i in range(len(tokens) - n + 1)]