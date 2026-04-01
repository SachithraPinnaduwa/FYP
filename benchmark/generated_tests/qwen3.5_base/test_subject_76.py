import unittest

class TestRingBuffer(unittest.TestCase):
    def setUp(self):
        self.buffer = RingBuffer(3)

    def test_initial_state(self):
        self.assertEqual(self.buffer.count, 0)
        self.assertEqual(self.buffer.is_empty(), True)
        self.assertEqual(self.buffer.is_full(), False)

    def test_enqueue_single_item(self):
        self.assertTrue(self.buffer.enqueue(1))
        self.assertEqual(self.buffer.count, 1)
        self.assertEqual(self.buffer.peek(), 1)
        self.assertEqual(self.buffer.is_empty(), False)
        self.assertEqual(self.buffer.is_full(), False)

    def test_enqueue_multiple_items(self):
        self.assertTrue(self.buffer.enqueue(1))
        self.assertTrue(self.buffer.enqueue(2))
        self.assertTrue(self.buffer.enqueue(3))
        self.assertEqual(self.buffer.count, 3)
        self.assertEqual(self.buffer.is_full(), True)
        self.assertEqual(self.buffer.peek(), 1)

    def test_enqueue_full_buffer(self):
        self.assertTrue(self.buffer.enqueue(1))
        self.assertTrue(self.buffer.enqueue(2))
        self.assertTrue(self.buffer.enqueue(3))
        self.assertFalse(self.buffer.enqueue(4))
        self.assertEqual(self.buffer.count, 3)

    def test_dequeue_single_item(self):
        self.buffer.enqueue(1)
        self.buffer.enqueue(2)
        self.assertEqual(self.buffer.dequeue(), 1)
        self.assertEqual(self.buffer.count, 1)
        self.assertEqual(self.buffer.peek(), 2)

    def test_dequeue_multiple_items(self):
        self.buffer.enqueue(1)
        self.buffer.enqueue(2)
        self.buffer.enqueue(3)
        self.assertEqual(self.buffer.dequeue(), 1)
        self.assertEqual(self.buffer.dequeue(), 2)
        self.assertEqual(self.buffer.count, 1)
        self.assertEqual(self.buffer.peek(), 3)

    def test_dequeue_empty_buffer(self):
        self.assertEqual(self.buffer.dequeue(), None)

    def test_peek_empty_buffer(self):
        self.assertEqual(self.buffer.peek(), None)

    def test_is_empty(self):
        self.assertTrue(self.buffer.is_empty())
        self.buffer.enqueue(1)
        self.assertFalse(self.buffer.is_empty())

    def test_is_full(self):
        self.assertFalse(self.buffer.is_full())
        self.buffer.enqueue(1)
        self.buffer.enqueue(2)
        self.buffer.enqueue(3)
        self.assertTrue(self.buffer.is_full())

    def test_wraparound(self):
        self.buffer.enqueue(1)
        self.buffer.enqueue(2)
        self.buffer.enqueue(3)
        self.buffer.enqueue(4)  # Should wrap around
        self.assertEqual(self.buffer.count, 3)
        self.assertEqual(self.buffer.peek(), 4)

    def test_wraparound_dequeue(self):
        self.buffer.enqueue(1)
        self.buffer.enqueue(2)
        self.buffer.enqueue(3)
        self.buffer.enqueue(4)
        self.buffer.enqueue(5)
        self.assertEqual(self.buffer.dequeue(), 1)
        self.assertEqual(self.buffer.dequeue(), 2)
        self.assertEqual(self.buffer.dequeue(), 3)
        self.assertEqual(self.buffer.count, 1)
        self.assertEqual(self.buffer.peek(), 5)

    def test_multiple_enqueues_and_dequeues(self):
        self.buffer.enqueue(1)
        self.buffer.enqueue(2)
        self.buffer.enqueue(3)
        self.assertEqual(self.buffer.dequeue(), 1)
        self.assertEqual(self.buffer.dequeue(), 2)
        self.assertEqual(self.buffer.dequeue(), 3)
        self.assertEqual(self.buffer.count, 0)
        self.assertTrue(self.buffer.is_empty())

    def test_enqueue_with_none(self):
        self.assertTrue(self.buffer.enqueue(None))
        self.assertEqual(self.buffer.count, 1)
        self.assertEqual(self.buffer.peek(), None)

    def test_enqueue_with_string(self):
        self.assertTrue(self.buffer.enqueue("hello"))
        self.assertEqual(self.buffer.count, 1)
        self.assertEqual(self.buffer.peek(), "hello")

    def test_enqueue_with_integer(self):
        self.assertTrue(self.buffer.enqueue(42))
        self.assertEqual(self.buffer.count, 1)
        self.assertEqual(self.buffer.peek(), 42)

    def test_enqueue_with_float(self):
        self.assertTrue(self.buffer.enqueue(3.14))
        self.assertEqual(self.buffer.count, 1)
        self.assertEqual(self.buffer.peek(), 3.14)

    def test_enqueue_with_list(self):
        self.assertTrue(self.buffer.enqueue([1, 2, 3]))
        self.assertEqual(self.buffer.count, 1)
        self.assertEqual(self.buffer.peek(), [1, 2, 3])

    def test_enqueue_with_tuple(self):
        self.assertTrue(self.buffer.enqueue((1, 2, 3)))
        self.assertEqual(self.buffer.count, 1)
        self.assertEqual(self.buffer.peek(), (1, 2, 3))

    def test_enqueue_with_dict(self):
        self.assertTrue(self.buffer.enqueue({"key": "value"}))
        self.assertEqual(self.buffer.count, 1)
        self.assertEqual(self.buffer.peek(), {"key": "value"})

    def test_enqueue_with_set(self):
        self.assertTrue(self.buffer.enqueue({1, 2, 3}))
        self.assertEqual(self.buffer.count, 1)
        self.assertEqual(self.buffer.peek(), {1, 2, 3})

    def test_enqueue_with_boolean(self):
        self.assertTrue(self.buffer.enqueue(True))
        self.assertEqual(self.buffer.count, 1)
        self.assertEqual(self.buffer.peek(), True)

    def test_enqueue_with_zero(self):
        self.assertTrue(self.buffer.enqueue(0))
        self.assertEqual(self.buffer.count, 1)
        self.assertEqual(self.buffer.peek(), 0)

    def test_enqueue_with_negative_integer(self):
        self.assertTrue(self.buffer.enqueue(-42))
        self.assertEqual(self.buffer.count, 1)
        self.assertEqual(self.buffer.peek(), -42)

    def test_enqueue_with_negative_float(self):
        self.assertTrue(self.buffer.enqueue(-3.14))
        self.assertEqual(self.buffer.count, 1)
        self.assertEqual(self.buffer.peek(), -3.14)

    def test_enqueue_with_empty_string(self):
        self.assertTrue(self.buffer.enqueue(""))
        self.assertEqual(self.buffer.count, 1)
        self.assertEqual(self.buffer.peek(), "")

    def test_enqueue_with_whitespace_string(self):
        self.assertTrue(self.buffer.enqueue("   "))
        self.assertEqual(self.buffer.count, 1)
        self.assertEqual(self.buffer.peek(), "   ")

    def test_enqueue_with_unicode_string(self):
        self.assertTrue(self.buffer.enqueue("你好"))
        self.assertEqual(self.buffer.count, 1)
        self.assertEqual(self.buffer.peek(), "你好")

    def test_enqueue_with_special_characters(self):
        self.assertTrue(self.buffer.enqueue("!@#$%^&*()"))
        self.assertEqual(self.buffer.count, 1)
        self.assertEqual(self.buffer.peek(), "!@#$%^&*()")

    def test_enqueue_with_newline(self):
        self.assertTrue(self