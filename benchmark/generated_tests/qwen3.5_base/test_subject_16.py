import unittest

class TestPriorityQueue(unittest.TestCase):
    def test_push_and_pop(self):
        pq = PriorityQueue()
        pq.push(1, 3)
        pq.push(2, 5)
        pq.push(3, 1)
        
        self.assertEqual(pq.pop(), 3)
        self.assertEqual(pq.pop(), 2)
        self.assertEqual(pq.pop(), 1)
        
    def test_push_and_peek(self):
        pq = PriorityQueue()
        pq.push(1, 3)
        pq.push(2, 5)
        pq.push(3, 1)
        
        self.assertEqual(pq.peek(), 3)
        
    def test_is_empty(self):
        pq = PriorityQueue()
        self.assertTrue(pq.is_empty())
        
        pq.push(1, 3)
        self.assertFalse(pq.is_empty())
        
    def test_multiple_pushes(self):
        pq = PriorityQueue()
        pq.push(1, 3)
        pq.push(2, 5)
        pq.push(3, 1)
        pq.push(4, 2)
        
        self.assertEqual(pq.pop(), 3)
        self.assertEqual(pq.pop(), 2)
        self.assertEqual(pq.pop(), 4)
        self.assertEqual(pq.pop(), 1)
        
    def test_priority_order(self):
        pq = PriorityQueue()
        pq.push(1, 3)
        pq.push(2, 5)
        pq.push(3, 1)
        
        self.assertEqual(pq.pop(), 3)
        self.assertEqual(pq.pop(), 2)
        self.assertEqual(pq.pop(), 1)
        
    def test_priority_order_with_equal_priorities(self):
        pq = PriorityQueue()
        pq.push(1, 3)
        pq.push(2, 3)
        pq.push(3, 3)
        
        self.assertEqual(pq.pop(), 1)
        self.assertEqual(pq.pop(), 2)
        self.assertEqual(pq.pop(), 3)
        
    def test_priority_order_with_negative_priorities(self):
        pq = PriorityQueue()
        pq.push(1, -3)
        pq.push(2, -5)
        pq.push(3, -1)
        
        self.assertEqual(pq.pop(), 3)
        self.assertEqual(pq.pop(), 1)
        self.assertEqual(pq.pop(), 2)
        
    def test_priority_order_with_mixed_priorities(self):
        pq = PriorityQueue()
        pq.push(1, 3)
        pq.push(2, -5)
        pq.push(3, 1)
        pq.push(4, -2)
        
        self.assertEqual(pq.pop(), 1)
        self.assertEqual(pq.pop(), 3)
        self.assertEqual(pq.pop(), 4)
        self.assertEqual(pq.pop(), 2)
        
    def test_priority_order_with_large_numbers(self):
        pq = PriorityQueue()
        pq.push(1, 1000000)
        pq.push(2, 1000000000)
        pq.push(3, 1)
        
        self.assertEqual(pq.pop(), 3)
        self.assertEqual(pq.pop(), 1)
        self.assertEqual(pq.pop(), 2)
        
    def test_priority_order_with_zero_priorities(self):
        pq = PriorityQueue()
        pq.push(1, 0)
        pq.push(2, 0)
        pq.push(3, 0)
        
        self.assertEqual(pq.pop(), 1)
        self.assertEqual(pq.pop(), 2)
        self.assertEqual(pq.pop(), 3)
        
    def test_priority_order_with_float_priorities(self):
        pq = PriorityQueue()
        pq.push(1, 3.5)
        pq.push(2, 5.2)
        pq.push(3, 1.1)
        
        self.assertEqual(pq.pop(), 3)
        self.assertEqual(pq.pop(), 2)
        self.assertEqual(pq.pop(), 1)
        
    def test_priority_order_with_string_priorities(self):
        pq = PriorityQueue()
        pq.push(1, "high")
        pq.push(2, "medium")
        pq.push(3, "low")
        
        self.assertEqual(pq.pop(), 1)
        self.assertEqual(pq.pop(), 2)
        self.assertEqual(pq.pop(), 3)
        
    def test_priority_order_with_none_priorities(self):
        pq = PriorityQueue()
        pq.push(1, None)
        pq.push(2, None)
        pq.push(3, None)
        
        self.assertEqual(pq.pop(), 1)
        self.assertEqual(pq.pop(), 2)
        self.assertEqual(pq.pop(), 3)
        
    def test_priority_order_with_list_priorities(self):
        pq = PriorityQueue()
        pq.push(1, [1, 2, 3])
        pq.push(2, [4, 5, 6])
        pq.push(3, [7, 8, 9])
        
        self.assertEqual(pq.pop(), 1)
        self.assertEqual(pq.pop(), 2)
        self.assertEqual(pq.pop(), 3)
        
    def test_priority_order_with_tuple_priorities(self):
        pq = PriorityQueue()
        pq.push(1, (1, 2, 3))
        pq.push(2, (4, 5, 6))
        pq.push(3, (7, 8, 9))
        
        self.assertEqual(pq.pop(), 1)
        self.assertEqual(pq.pop(), 2)
        self.assertEqual(pq.pop(), 3)
        
    def test_priority_order_with_dict_priorities(self):
        pq = PriorityQueue()
        pq.push(1, {"a": 1, "b": 2})
        pq.push(2, {"c": 3, "d": 4})
        pq.push(3, {"e": 5, "f": 6})
        
        self.assertEqual(pq.pop(), 1)
        self.assertEqual(pq.pop(), 2)
        self.assertEqual(pq.pop(), 3)
        
    def test_priority_order_with_set_priorities(self):
        pq = PriorityQueue()
        pq.push(1, {1, 2, 3})
        pq.push(2, {4, 5, 6})
        pq.push(3, {7, 8, 9})
        
        self.assertEqual(pq.pop(), 1)
        self.assertEqual(pq.pop(), 2)
        self.assertEqual(pq.pop(), 3)
        
    def test_priority_order_with_bool_priorities(self):
        pq = PriorityQueue()
        pq.push(1, True)
        pq.push(2, False)
        pq.push(3, True)
        
        self.assertEqual