import time

class LeakyBucketLimiter:
    def __init__(self, capacity: float, leak_rate: float):
        self.capacity = capacity
        self.leak_rate = leak_rate
        self.current_level = 0.0
        self.last_update = time.monotonic()

    def allow_request(self, drop_size: float = 1.0) -> bool:
        now = time.monotonic()
        elapsed = now - self.last_update
        
        leaked = elapsed * self.leak_rate
        self.current_level = max(0.0, self.current_level - leaked)
        self.last_update = now
        
        if self.current_level + drop_size <= self.capacity:
            self.current_level += drop_size
            return True
            
        return False