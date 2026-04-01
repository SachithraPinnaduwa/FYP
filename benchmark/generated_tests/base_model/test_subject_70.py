import unittest

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseLinkedList(head):
    previous = None
    current = head

    while current:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node

    return previous

class TestReverseLinkedList(unittest.TestCase):

    def test_reverse_linked_list(self):
        # Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        
        # Reverse the linked list
        reversed_head = reverseLinkedList(head)
        
        # Check if the reversed linked list is correct: 5 -> 4 -> 3 -> 2 -> 1
        expected_values = [5, 4, 3, 2, 1]
        current = reversed_head
        for value in expected_values:
            self.assertEqual(current.val, value)
            current = current.next
        
        # Ensure there are no more nodes after the last one
        self.assertIsNone(current)

    def test_single_node_list(self):
        # Create a single-node linked list: 7
        head = ListNode(7)
        
        # Reverse the linked list
        reversed_head = reverseLinkedList(head)
        
        # Check if the reversed linked list is the same single node
        self.assertEqual(reversed_head.val, 7)
        self.assertIsNone(reversed_head.next)

    def test_empty_list(self):
        # Call reverse on an empty list (None)
        reversed_head = reverseLinkedList(None)
        
        # Check if the result is None
        self.assertIsNone(reversed_head)

if __name__ == '__main__':
    unittest.main()