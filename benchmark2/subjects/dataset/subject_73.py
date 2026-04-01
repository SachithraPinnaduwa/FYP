import math

class TfIdfScorer:
    def __init__(self):
        self.documents = {}
        self.doc_freq = {}
        self.total_docs = 0

    def add_document(self, doc_id: str, text: str):
        words = text.lower().split()
        word_counts = {}
        for w in words:
            word_counts[w] = word_counts.get(w, 0) + 1
            
        self.documents[doc_id] = word_counts
        
        for w in set(words):
            self.doc_freq[w] = self.doc_freq.get(w, 0) + 1
            
        self.total_docs += 1

    def get_score(self, word: str, doc_id: str) -> float:
        if doc_id not in self.documents:
            return 0.0
            
        word = word.lower()
        if word not in self.documents[doc_id]:
            return 0.0
            
        tf = self.documents[doc_id][word]
        idf = math.log((self.total_docs + 1) / (self.doc_freq.get(word, 0) + 1)) + 1
        return tf * idf