class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.freqs = {}
        self.min_freq = 0

    def get(self, key):
        if key not in self.cache:
            return None
        value, f = self.cache[key]
        self.freqs[f].remove(key)
        if not self.freqs[f] and self.min_freq == f:
            self.min_freq += 1
        self.freqs.setdefault(f + 1, []).append(key)
        self.cache[key] = (value, f + 1)
        return value

    def put(self, key, value):
        if self.capacity <= 0:
            return
        if key in self.cache:
            _, f = self.cache[key]
            self.cache[key] = (value, f)
            self.get(key)
            return
        if len(self.cache) >= self.capacity:
            evict = self.freqs[self.min_freq].pop(0)
            del self.cache[evict]
        self.cache[key] = (value, 1)
        self.freqs.setdefault(1, []).append(key)
        self.min_freq = 1