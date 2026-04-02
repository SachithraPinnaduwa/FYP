from subject_70 import *

import unittest

class TestReverseLinkedList(unittest.TestCase):
    def test_reverse_linked_list_multiple_nodes(self):
        # Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        # Expected reversed linked list: 5 -> 4 -> 3 -> 2 -> 1
        expected = ListNode(5, ListNode(4, ListNode(3, ListNode(2, ListNode(1)))))
        # Call the function to reverse the linked list
        result = reverseLinkedList(head)
        # Check if the reversed linked list matches the expected result
        self.assertEqual(result, expected)

    def test_reverse_linked_list_single_node(self):
        # Create a linked list with a single node: 1
        head = ListNode(1)
        # Expected reversed linked list: 1
        expected = ListNode(1)
        # Call the function to reverse the linked list
        result = reverseLinkedList(head)
        # Check if the reversed linked list matches the expected result
        self.assertEqual(result, expected)

    def test_reverse_linked_list_empty_list(self):
        # Call the function with an empty linked list
        result = reverseLinkedList(None)
        # Check if the result is None
        self.assertIsNone(result)

    def test_reverse_linked_list_two_nodes(self):
        # Create a linked list with two nodes: 1 -> 2
        head = ListNode(1, ListNode(2))
        # Expected reversed linked list: 2 -> 1
        expected = ListNode(2, ListNode(1))
        # Call the function to reverse the linked list
        result = reverseLinkedList(head)
        # Check if the reversed linked list matches the expected result
        self.assertEqual(result, expected)

    def test_reverse_linked_list_none_input(self):
        # Call the function with None as the input
        result = reverseLinkedList(None)
        # Check if the result is None
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()