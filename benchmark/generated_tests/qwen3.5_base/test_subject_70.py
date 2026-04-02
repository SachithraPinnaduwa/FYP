import unittest

class TestReverseLinkedList(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(reverseLinkedList(None), None)

    def test_single_node(self):
        node = ListNode(1)
        self.assertEqual(reverseLinkedList(node).val, 1)
        self.assertIsNone(reverseLinkedList(node).next)

    def test_two_nodes(self):
        node1 = ListNode(1)
        node2 = ListNode(2, None)
        node1.next = node2
        reversed_list = reverseLinkedList(node1)
        self.assertEqual(reversed_list.val, 2)
        self.assertEqual(reversed_list.next.val, 1)
        self.assertIsNone(reversed_list.next.next)

    def test_three_nodes(self):
        node1 = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)
        node1.next = node2
        node2.next = node3
        reversed_list = reverseLinkedList(node1)
        self.assertEqual(reversed_list.val, 3)
        self.assertEqual(reversed_list.next.val, 2)
        self.assertEqual(reversed_list.next.next.val, 1)
        self.assertIsNone(reversed_list.next.next.next)

    def test_large_list(self):
        # Create a list of 10 nodes
        nodes = [ListNode(i) for i in range(1, 11)]
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        reversed_list = reverseLinkedList(nodes[0])
        self.assertEqual(reversed_list.val, 10)
        self.assertEqual(reversed_list.next.val, 9)
        self.assertEqual(reversed_list.next.next.val, 8)
        self.assertEqual(reversed_list.next.next.next.val, 7)
        self.assertEqual(reversed_list.next.next.next.next.val, 6)
        self.assertEqual(reversed_list.next.next.next.next.next.val, 5)
        self.assertEqual(reversed_list.next.next.next.next.next.next.val, 4)
        self.assertEqual(reversed_list.next.next.next.next.next.next.next.val, 3)
        self.assertEqual(reversed_list.next.next.next.next.next.next.next.next.val, 2)
        self.assertEqual(reversed_list.next.next.next.next.next.next.next.next.next.val, 1)
        self.assertIsNone(reversed_list.next.next.next.next.next.next.next.next.next.next)

if __name__ == '__main__':
    unittest.main()
