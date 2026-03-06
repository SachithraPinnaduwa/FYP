"""
Linked List module - Subject for test generation benchmarking.
Contains singly linked list implementation with various operations.
"""

from typing import Any, Optional, List


class Node:
    """A node in a singly linked list."""

    def __init__(self, data: Any, next_node: Optional['Node'] = None):
        self.data = data
        self.next = next_node

    def __repr__(self) -> str:
        return f"Node({self.data})"


class LinkedList:
    """
    A singly linked list implementation.
    """

    def __init__(self):
        """Initialize an empty linked list."""
        self._head: Optional[Node] = None
        self._size: int = 0

    @property
    def head(self) -> Optional[Node]:
        return self._head

    @property
    def size(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        """Check if the list is empty."""
        return self._head is None

    def append(self, data: Any) -> None:
        """Add an element to the end of the list."""
        new_node = Node(data)
        if self._head is None:
            self._head = new_node
        else:
            current = self._head
            while current.next:
                current = current.next
            current.next = new_node
        self._size += 1

    def prepend(self, data: Any) -> None:
        """Add an element to the beginning of the list."""
        new_node = Node(data, self._head)
        self._head = new_node
        self._size += 1

    def insert_at(self, index: int, data: Any) -> None:
        """
        Insert an element at a specific index.

        Args:
            index: Position to insert at (0-based)
            data: Data to insert

        Raises:
            IndexError: If index is out of range
        """
        if index < 0 or index > self._size:
            raise IndexError(f"Index {index} out of range for list of size {self._size}")
        if index == 0:
            self.prepend(data)
            return
        current = self._head
        for _ in range(index - 1):
            current = current.next
        new_node = Node(data, current.next)
        current.next = new_node
        self._size += 1

    def remove(self, data: Any) -> bool:
        """
        Remove the first occurrence of data from the list.

        Returns:
            True if the element was found and removed, False otherwise
        """
        if self._head is None:
            return False
        if self._head.data == data:
            self._head = self._head.next
            self._size -= 1
            return True
        current = self._head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                self._size -= 1
                return True
            current = current.next
        return False

    def remove_at(self, index: int) -> Any:
        """
        Remove and return the element at the given index.

        Raises:
            IndexError: If the list is empty or index is out of range
        """
        if self._head is None:
            raise IndexError("Cannot remove from empty list")
        if index < 0 or index >= self._size:
            raise IndexError(f"Index {index} out of range for list of size {self._size}")
        if index == 0:
            data = self._head.data
            self._head = self._head.next
            self._size -= 1
            return data
        current = self._head
        for _ in range(index - 1):
            current = current.next
        data = current.next.data
        current.next = current.next.next
        self._size -= 1
        return data

    def get(self, index: int) -> Any:
        """
        Get the element at the given index.

        Raises:
            IndexError: If index is out of range
        """
        if index < 0 or index >= self._size:
            raise IndexError(f"Index {index} out of range for list of size {self._size}")
        current = self._head
        for _ in range(index):
            current = current.next
        return current.data

    def find(self, data: Any) -> int:
        """
        Find the index of the first occurrence of data.

        Returns:
            The index, or -1 if not found
        """
        current = self._head
        index = 0
        while current:
            if current.data == data:
                return index
            current = current.next
            index += 1
        return -1

    def contains(self, data: Any) -> bool:
        """Check if the list contains the given data."""
        return self.find(data) != -1

    def to_list(self) -> List[Any]:
        """Convert the linked list to a Python list."""
        result = []
        current = self._head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def reverse(self) -> None:
        """Reverse the linked list in place."""
        prev = None
        current = self._head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self._head = prev

    def clear(self) -> None:
        """Remove all elements from the list."""
        self._head = None
        self._size = 0

    def __len__(self) -> int:
        return self._size

    def __repr__(self) -> str:
        elements = self.to_list()
        return f"LinkedList({' -> '.join(str(e) for e in elements)})"

    def __contains__(self, data: Any) -> bool:
        return self.contains(data)


def merge_sorted_lists(list1: 'LinkedList', list2: 'LinkedList') -> 'LinkedList':
    """
    Merge two sorted linked lists into a new sorted linked list.

    Args:
        list1: First sorted linked list
        list2: Second sorted linked list

    Returns:
        A new sorted linked list
    """
    result = LinkedList()
    items = sorted(list1.to_list() + list2.to_list())
    for item in items:
        result.append(item)
    return result
