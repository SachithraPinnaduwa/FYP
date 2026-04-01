import time
import uuid

class TemporalCache:
    def __init__(self):
        self.storage = {}

    def put(self, key: str, value: any):
        if key not in self.storage:
            self.storage[key] = []
        self.storage[key].append({
            "val": value,
            "version": str(uuid.uuid4()),
            "ts": time.time()
        })

    def get_latest(self, key: str) -> any:
        if key not in self.storage or not self.storage[key]:
            return None
        return self.storage[key][-1]["val"]

    def get_as_of(self, key: str, timestamp: float) -> any:
        if key not in self.storage:
            return None
            
        history = self.storage[key]
        for idx in range(len(history)-1, -1, -1):
            if history[idx]["ts"] <= timestamp:
                return history[idx]["val"]
        return None