class TokenBucket:
    def __init__(self, capacity: int, refill_rate: float):
        import time
        self.capacity = capacity
        self.refill_rate = refill_rate
        self.tokens = float(capacity)
        self.last_refill = time.monotonic()

    def consume(self, tokens: int = 1) -> bool:
        self._refill()
        if self.tokens >= tokens:
            self.tokens -= tokens
            return True
        return False

    def _refill(self):
        import time
        now = time.monotonic()
        delta = now - self.last_refill
        self.tokens = min(self.capacity, self.tokens + delta * self.refill_rate)
        self.last_refill = now

    def time_until_next_token(self) -> float:
        if self.tokens >= 1:
            return 0.0
        return (1.0 - self.tokens) / self.refill_rate