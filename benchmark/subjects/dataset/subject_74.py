import time
from collections import deque

class SlidingWindowAverage:
    def __init__(self, window_size_seconds: float):
        self.window = window_size_seconds
        self.queue = deque()
        self.total_sum = 0.0

    def add(self, value: float):
        now = time.monotonic()
        self.queue.append({"val": value, "time": now})
        self.total_sum += value
        self._prune(now)

    def _prune(self, now: float):
        while self.queue and now - self.queue[0]["time"] > self.window:
            item = self.queue.popleft()
            self.total_sum -= item["val"]

    def get_average(self) -> float:
        self._prune(time.monotonic())
        if not self.queue:
            return 0.0
        return self.total_sum / len(self.queue)