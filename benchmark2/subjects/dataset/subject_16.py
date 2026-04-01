import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        if not self._queue:
            return None
        return heapq.heappop(self._queue)[-1]
        
    def peek(self):
        if not self._queue: return None
        return self._queue[0][-1]
        
    def is_empty(self):
        return len(self._queue) == 0