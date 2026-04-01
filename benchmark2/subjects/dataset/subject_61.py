class DocumentIndexer:
    def __init__(self):
        self.index = {}
        self.doc_store = {}

    def add_document(self, doc_id: int, content: str):
        self.doc_store[doc_id] = content
        words = content.lower().split()
        for pos, word in enumerate(words):
            word = "".join(c for c in word if c.isalnum())
            if not word:
                continue
            if word not in self.index:
                self.index[word] = {}
            if doc_id not in self.index[word]:
                self.index[word][doc_id] = []
            self.index[word][doc_id].append(pos)

    def search(self, phrase: str) -> list:
        words = ["".join(c for c in w if c.isalnum()) for w in phrase.lower().split()]
        if not words or not all(w in self.index for w in words):
            return []

        # Find docs that contain all words
        first_word = words[0]
        common_docs = set(self.index[first_word].keys())
        for w in words[1:]:
            common_docs &= set(self.index[w].keys())

        return sorted(list(common_docs))