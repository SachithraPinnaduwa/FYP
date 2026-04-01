class AutoCorrector:
    def __init__(self, dictionary: set):
        self.dictionary = {word.lower() for word in dictionary}

    def _levenshtein(self, s1: str, s2: str) -> int:
        if len(s1) < len(s2):
            return self._levenshtein(s2, s1)
        if len(s2) == 0:
            return len(s1)
            
        previous_row = range(len(s2) + 1)
        for i, c1 in enumerate(s1):
            current_row = [i + 1]
            for j, c2 in enumerate(s2):
                insertions = previous_row[j + 1] + 1
                deletions = current_row[j] + 1
                substitutions = previous_row[j] + (c1 != c2)
                current_row.append(min(insertions, deletions, substitutions))
            previous_row = current_row
        return previous_row[-1]

    def correct(self, word: str, max_distance: int = 2) -> list:
        word = word.lower()
        if word in self.dictionary:
            return [word]
            
        candidates = []
        for dict_word in self.dictionary:
            dist = self._levenshtein(word, dict_word)
            if dist <= max_distance:
                candidates.append((dict_word, dist))
                
        candidates.sort(key=lambda x: x[1])
        return [c[0] for c in candidates]