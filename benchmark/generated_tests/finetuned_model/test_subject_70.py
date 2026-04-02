import unittest

class TestReverseLinkedList(unittest.TestCase):
    def test_reverse_linked_list(self):
        # Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
        node1 = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)
        node4 = ListNode(4)
        node5 = ListNode(5)
        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node5

        # Reverse the linked list
        reversed_head = reverseLinkedList(node1)

        # Check if the reversed linked list is correct
        self.assertEqual(reversed_head.val, 5)
        self.assertEqual(reversed_head.next.val, 4)
        self.assertEqual(reversed_head.next.next.val, 3)
        self.assertEqual(reversed_head.next.next.next.val, 2)
        self.assertEqual(reversed_head.next.next.next.next.val, 1)
        self.assertIsNone(reversed_head.next.next.next.next.next)

    def test_single_node(self):
        # Create a linked list with a single node: 7
        node7 = ListNode(7)

        # Reverse the linked list
        reversed_head = reverseLinkedList(node7)

        # Check if the reversed linked list is correct
        self.assertEqual(reversed_head.val, 7)
        self.assertIsNone(reversed_head.next)

    def test_empty_list(self):
        # Reverse an empty linked list
        reversed_head = reverseLinkedList(None)

        # Check if the reversed linked list is None
        self.assertIsNone(reversed_head)

if __name__ == '__main__':
    unittest.main()