class MinMaxHeap:
    def __init__(self):
        self.heap = []

    def push(self, val):
        self.heap.append(val)
        self.heap.sort()

    def pop_min(self):
        if not self.heap: return None
        return self.heap.pop(0)

    def pop_max(self):
        if not self.heap: return None
        return self.heap.pop()

    def peek_min(self):
        return self.heap[0] if self.heap else None

    def peek_max(self):
        return self.heap[-1] if self.heap else None
        
    def size(self):
        return len(self.heap)