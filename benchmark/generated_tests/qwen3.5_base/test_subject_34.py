import unittest

class TestSimpleConnectionPool(unittest.TestCase):
    def setUp(self):
        self.mock_factory = lambda: "mock_connection"
        self.pool = SimpleConnectionPool(max_size=2, factory=self.mock_factory)

    def test_acquire_returns_connection(self):
        conn = self.pool.acquire()
        self.assertEqual(conn, "mock_connection")

    def test_acquire_exceeds_max_size(self):
        for _ in range(3):
            self.pool.acquire()
        with self.assertRaises(Exception):
            self.pool.acquire()

    def test_release_connection(self):
        conn = self.pool.acquire()
        self.pool.release(conn)
        self.assertEqual(self.pool.active_connections(), 0)

    def test_active_connections(self):
        self.pool.acquire()
        self.assertEqual(self.pool.active_connections(), 1)

    def test_close_all(self):
        self.pool.acquire()
        self.pool.acquire()
        self.pool.close_all()
        self.assertEqual(self.pool.active_connections(), 0)

if __name__ == '__main__':
    unittest.main()
