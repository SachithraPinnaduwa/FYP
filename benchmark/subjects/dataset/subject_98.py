class BloomFilterHash:
    def __init__(self, capacity: int = 100):
        self.size = capacity
        self.bits = 0
        
    def _hash1(self, string: str) -> int:
        return sum(ord(c) for c in string) % self.size
        
    def _hash2(self, string: str) -> int:
        return sum(ord(c) * (i+1) for i, c in enumerate(string)) % self.size
        
    def _hash3(self, string: str) -> int:
        return sum(ord(c) ^ (i+1) for i, c in enumerate(string)) % self.size

    def insert(self, string: str):
        self.bits |= (1 << self._hash1(string))
        self.bits |= (1 << self._hash2(string))
        self.bits |= (1 << self._hash3(string))

    def contains(self, string: str) -> bool:
        h1 = (self.bits & (1 << self._hash1(string))) > 0
        h2 = (self.bits & (1 << self._hash2(string))) > 0
        h3 = (self.bits & (1 << self._hash3(string))) > 0
        return h1 and h2 and h3