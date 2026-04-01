import time
class RateLimiter:
    def __init__(self, cap, rate):
        self.cap, self.rate = float(cap), rate
        self.tokens, self.last = float(cap), time.monotonic()
    def take(self, amount):
        now = time.monotonic()
        self.tokens = min(self.cap, self.tokens + (now - self.last) * self.rate)
        self.last = now
        if self.tokens >= amount:
            self.tokens -= amount
            return True
        return False
