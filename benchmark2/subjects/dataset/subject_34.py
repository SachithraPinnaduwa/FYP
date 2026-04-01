class SimpleConnectionPool:
    def __init__(self, max_size: int, factory):
        self.max_size = max_size
        self.factory = factory
        self.pool = []
        self.in_use = set()

    def acquire(self):
        if self.pool:
            conn = self.pool.pop()
        elif len(self.in_use) < self.max_size:
            conn = self.factory()
        else:
            raise Exception("Pool exhausted")
            
        self.in_use.add(conn)
        return conn

    def release(self, conn):
        if conn in self.in_use:
            self.in_use.remove(conn)
            self.pool.append(conn)

    def active_connections(self) -> int:
        return len(self.in_use)

    def close_all(self):
        self.pool.clear()
        self.in_use.clear()