import hashlib

class FileHasher:
    def __init__(self, alg: str = 'sha256'):
        self.alg = alg
        
    def hash_string(self, text: str) -> str:
        h = hashlib.new(self.alg)
        h.update(text.encode('utf-8'))
        return h.hexdigest()

    def check_integrity(self, text: str, expected_hash: str) -> bool:
        return self.hash_string(text) == expected_hash