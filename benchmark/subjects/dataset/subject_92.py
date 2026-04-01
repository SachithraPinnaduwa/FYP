class LifecycleObjectPool:
    def __init__(self, factory, reset, max_size: int = 10):
        self.factory = factory
        self.reset = reset
        self.max_size = max_size
        self.pool = []
        self.in_use = set()

    def acquire(self):
        if self.pool:
            obj = self.pool.pop()
            self.reset(obj)
        elif len(self.in_use) < self.max_size:
            obj = self.factory()
        else:
            raise RuntimeError("Pool is empty and at maximum capacity")
            
        self.in_use.add(obj)
        return obj

    def release(self, obj):
        if obj in self.in_use:
            self.in_use.remove(obj)
            if len(self.pool) < self.max_size:
                self.pool.append(obj)
            else:
                pass # let it be garbage collected