import hashlib
import math

class BloomFilter:
    def __init__(self, items_count: int, fp_prob: float):
        self.fp_prob = fp_prob
        self.size = self._get_size(items_count, fp_prob)
        self.hash_count = self._get_hash_count(self.size, items_count)
        self.bit_array = bytearray((self.size + 7) // 8)

    def _get_size(self, n: int, p: float) -> int:
        return int(-(n * math.log(p)) / (math.log(2) ** 2))

    def _get_hash_count(self, m: int, n: int) -> int:
        return int((m / n) * math.log(2))

    def add(self, item: str):
        for i in range(self.hash_count):
            digest = hashlib.sha256(f"{item}{i}".encode('utf8')).hexdigest()
            index = int(digest, 16) % self.size
            self.bit_array[index // 8] |= (1 << (index % 8))

    def check(self, item: str) -> bool:
        for i in range(self.hash_count):
            digest = hashlib.sha256(f"{item}{i}".encode('utf8')).hexdigest()
            index = int(digest, 16) % self.size
            if not (self.bit_array[index // 8] & (1 << (index % 8))):
                return False
        return True