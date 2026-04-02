import unittest

class TestReverseLinkedList(unittest.TestCase):

    def test_reverse_linked_list(self):
        # Create a sample linked list: 1 -> 2 -> 3 -> 4 -> 5
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)
        head.next.next.next.next = ListNode(5)

        # Reverse the linked list
        new_head = reverseLinkedList(head)

        # Check if the reversed linked list is correct: 5 -> 4 -> 3 -> 2 -> 1
        values = []
        while new_head:
            values.append(new_head.val)
            new_head = new_head.next

        self.assertEqual(values, [5, 4, 3, 2, 1])

    def test_empty_list(self):
        # Test reversing an empty list
        new_head = reverseLinkedList(None)
        self.assertIsNone(new_head)

    def test_single_element_list(self):
        # Test reversing a list with a single element
        head = ListNode(1)
        new_head = reverseLinkedList(head)
        self.assertEqual(new_head.val, 1)
        self.assertIsNone(new_head.next)

if __name__ == '__main__':
    unittest.main()