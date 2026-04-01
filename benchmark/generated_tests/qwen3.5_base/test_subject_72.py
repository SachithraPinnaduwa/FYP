import unittest

class TestMinMaxHeap(unittest.TestCase):
    def setUp(self):
        self.heap = MinMaxHeap()

    def test_push_and_pop_min(self):
        self.heap.push(3)
        self.heap.push(1)
        self.heap.push(5)
        self.assertEqual(self.heap.pop_min(), 1)
        self.assertEqual(self.heap.pop_min(), 3)
        self.assertEqual(self.heap.pop_min(), 5)

    def test_push_and_pop_max(self):
        self.heap.push(3)
        self.heap.push(1)
        self.heap.push(5)
        self.assertEqual(self.heap.pop_max(), 5)
        self.assertEqual(self.heap.pop_max(), 3)
        self.assertEqual(self.heap.pop_max(), 1)

    def test_peek_min_and_max(self):
        self.heap.push(3)
        self.heap.push(1)
        self.heap.push(5)
        self.assertEqual(self.heap.peek_min(), 1)
        self.assertEqual(self.heap.peek_max(), 5)

    def test_size(self):
        self.heap.push(3)
        self.heap.push(1)
        self.heap.push(5)
        self.assertEqual(self.heap.size(), 3)

    def test_empty_operations(self):
        self.assertEqual(self.heap.pop_min(), None)
        self.assertEqual(self.heap.pop_max(), None)
        self.assertEqual(self.heap.peek_min(), None)
        self.assertEqual(self.heap.peek_max(), None)
        self.assertEqual(self.heap.size(), 0)

if __name__ == '__main__':
    unittest.main()
