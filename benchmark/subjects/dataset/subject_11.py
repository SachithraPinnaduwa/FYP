import time
class TTLCache:
    def __init__(self): self.store = {}
    def set(self, key, val, ttl):
        self.store[key] = (val, time.time() + ttl)
    def get(self, key):
        if key in self.store:
            val, exp = self.store[key]
            if time.time() < exp: return val
            del self.store[key]
        return None
