import unittest

class TestReverseLinkedList(unittest.TestCase):

    def test_reverse_linked_list_with_single_node(self):
        # Create a linked list with a single node
        node = ListNode(1)
        # Reverse the linked list
        reversed_head = reverseLinkedList(node)
        # Check if the reversed linked list has the same head
        self.assertEqual(reversed_head.val, 1)
        # Check if the reversed linked list has the same next node
        self.assertIsNone(reversed_head.next)

    def test_reverse_linked_list_with_multiple_nodes(self):
        # Create a linked list with multiple nodes
        node1 = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)
        node1.next = node2
        node2.next = node3
        # Reverse the linked list
        reversed_head = reverseLinkedList(node1)
        # Check if the reversed linked list has the correct order
        self.assertEqual(reversed_head.val, 3)
        self.assertEqual(reversed_head.next.val, 2)
        self.assertEqual(reversed_head.next.next.val, 1)
        # Check if the reversed linked list has the correct next node for the last node
        self.assertIsNone(reversed_head.next.next.next)

    def test_reverse_linked_list_with_empty_list(self):
        # Create an empty linked list
        node = None
        # Reverse the linked list
        reversed_head = reverseLinkedList(node)
        # Check if the reversed linked list is None
        self.assertIsNone(reversed_head)

    def test_reverse_linked_list_with_two_nodes(self):
        # Create a linked list with two nodes
        node1 = ListNode(1)
        node2 = ListNode(2)
        node1.next = node2
        # Reverse the linked list
        reversed_head = reverseLinkedList(node1)
        # Check if the reversed linked list has the correct order
        self.assertEqual(reversed_head.val, 2)
        self.assertEqual(reversed_head.next.val, 1)
        # Check if the reversed linked list has the correct next node for the last node
        self.assertIsNone(reversed_head.next.next)