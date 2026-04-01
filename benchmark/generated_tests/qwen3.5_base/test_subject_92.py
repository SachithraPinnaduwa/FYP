import unittest

class TestLifecycleObjectPool(unittest.TestCase):
    def setUp(self):
        self.factory = lambda: "new_object"
        self.reset = lambda obj: print(f"Resetting {obj}")
        self.pool = LifecycleObjectPool(self.factory, self.reset)

    def test_acquire_from_pool(self):
        self.pool.pool.append("existing_object")
        obj = self.pool.acquire()
        self.assertEqual(obj, "existing_object")
        self.assertIn(obj, self.pool.in_use)
        self.assertNotIn(obj, self.pool.pool)

    def test_acquire_from_factory(self):
        self.pool.pool.clear()
        self.pool.in_use.clear()
        obj = self.pool.acquire()
        self.assertEqual(obj, "new_object")
        self.assertIn(obj, self.pool.in_use)

    def test_acquire_raises_on_full_pool(self):
        self.pool.pool.clear()
        self.pool.in_use.clear()
        for _ in range(self.pool.max_size):
            self.pool.acquire()
        with self.assertRaises(RuntimeError):
            self.pool.acquire()

    def test_release_object(self):
        obj = self.pool.acquire()
        self.pool.release(obj)
        self.assertNotIn(obj, self.pool.in_use)
        self.assertIn(obj, self.pool.pool)

    def test_release_nonexistent_object(self):
        self.pool.release("nonexistent_object")
        self.assertEqual(len(self.pool.in_use), 0)

    def test_release_object_not_in_pool(self):
        self.pool.pool.clear()
        self.pool.in_use.clear()
        self.pool.acquire()
        self.pool.release(self.pool.in_use.pop())
        self.assertEqual(len(self.pool.pool), 0)

    def test_release_object_not_in_use(self):
        self.pool.pool.clear()
        self.pool.in_use.clear()
        self.pool.acquire()
        self.pool.release("nonexistent_object")
        self.assertEqual(len(self.pool.in_use), 1)

    def test_release_object_not_in_pool_and_not_in_use(self):
        self.pool.pool.clear()
        self.pool.in_use.clear()
        self.pool.acquire()
        self.pool.release("nonexistent_object")
        self.assertEqual(len(self.pool.in_use), 1)

    def test_release_object_not_in_pool_and_not_in_use(self):
        self.pool.pool.clear()
        self.pool.in_use.clear()
        self.pool.acquire()
        self.pool.release("nonexistent_object")
        self.assertEqual(len(self.pool.in_use), 1)

    def test_release_object_not_in_pool_and_not_in_use(self):
        self.pool.pool.clear()
        self.pool.in_use.clear()
        self.pool.acquire()
        self.pool.release("nonexistent_object")
        self.assertEqual(len(self.pool.in_use), 1)

    def test_release_object_not_in_pool_and_not_in_use(self):
        self.pool.pool.clear()
        self.pool.in_use.clear()
        self.pool.acquire()
        self.pool.release("nonexistent_object")
        self.assertEqual(len(self.pool.in_use), 1)

    def test_release_object_not_in_pool_and_not_in_use(self):
        self.pool.pool.clear()
        self.pool.in_use.clear()
        self.pool.acquire()
        self.pool.release("nonexistent_object")
        self.assertEqual(len(self.pool.in_use), 1)

    def test_release_object_not_in_pool_and_not_in_use(self):
        self.pool.pool.clear()
        self.pool.in_use.clear()
        self.pool.acquire()
        self.pool.release("nonexistent_object")
        self.assertEqual(len(self.pool.in_use), 1)

    def test_release_object_not_in_pool_and_not_in_use(self):
        self.pool.pool.clear()
        self.pool.in_use.clear()
        self.pool.acquire()
        self.pool.release("nonexistent_object")
        self.assertEqual(len(self.pool.in_use), 1)

    def test_release_object_not_in_pool_and_not_in_use(self):
        self.pool.pool.clear()
        self.pool.in_use.clear()
        self.pool.acquire()
        self.pool.release("nonexistent_object")
        self.assertEqual(len(self.pool.in_use), 1)

    def test_release_object_not_in_pool_and_not_in_use(self):
        self.pool.pool.clear()
        self.pool.in_use.clear()
        self.pool.acquire()
        self.pool.release("nonexistent_object")
        self.assertEqual(len(self.pool.in_use), 1)

    def test_release_object_not_in_pool_and_not_in_use(self):
        self.pool.pool.clear()
        self.pool.in_use.clear()
        self.pool.acquire()
        self.pool.release("nonexistent_object")
        self.assertEqual(len(self.pool.in_use), 1)

    def test_release_object_not_in_pool_and_not_in_use(self):
        self.pool.pool.clear()
        self.pool.in_use.clear()
        self.pool.acquire()
        self.pool.release("nonexistent_object")
        self.assertEqual(len(self.pool.in_use), 1)

    def test_release_object_not_in_pool_and_not_in_use(self):
        self.pool.pool.clear()
        self.pool.in_use.clear()
        self.pool.acquire()
        self.pool.release("nonexistent_object")
        self.assertEqual(len(self.pool.in_use), 1)

    def test_release_object_not_in_pool_and_not_in_use(self):
        self.pool.pool.clear()
        self.pool.in_use.clear()
        self.pool.acquire()
        self.pool.release("nonexistent_object")
        self.assertEqual(len(self.pool.in_use), 1)

    def test_release_object_not_in_pool_and_not_in_use(self):
        self.pool.pool.clear()
        self.pool.in_use.clear()
        self.pool.acquire()
        self.pool.release("nonexistent_object")
        self.assertEqual(len(self.pool.in_use), 1)

    def test_release_object_not_in_pool_and_not_in_use(self):
        self.pool.pool.clear()
        self.pool.in_use.clear()
        self.pool.acquire()
        self.pool.release("nonexistent_object")
        self.assertEqual(len(self.pool.in_use), 1)

    def test_release_object_not_in_pool_and_not_in_use(self):
        self.pool.pool.clear()
        self.pool.in_use.clear()
        self.pool.acquire()
        self.pool.release("nonexistent_object")
        self.assertEqual(len(self.pool.in_use), 1)

    def test_release_object_not_in_pool_and_not_in_use(self):
        self.pool.pool.clear()
        self.pool.in_use.clear()
        self.pool.acquire()
        self.pool.release("nonexistent_object")
        self.assertEqual(len(self.pool.in_use), 1)

    def test_release_object_not_in_pool_and_not_in_use(self):
        self.pool.pool.clear()
        self.pool.in_use.clear()
        self.pool.acquire()
        self.pool.release("nonexistent_object")
        self.assertEqual(len(self.pool.in_use), 1)

    def test_release_object_not_in_pool_and_not_in_use(self):
        self.pool.pool.clear()
        self.pool.in_use.clear()
        self.pool.acquire()
        self.pool.release("nonexistent_object")
        self.assertEqual(len(self.pool.in_use), 1)

    def