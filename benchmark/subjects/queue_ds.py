"""
Queue module - Subject for test generation benchmarking.
Contains queue and priority queue implementations.
"""

from typing import Any, List, Optional, Tuple
import heapq


class QueueEmptyError(Exception):
    """Raised when trying to dequeue from an empty queue."""
    pass


class QueueFullError(Exception):
    """Raised when trying to enqueue to a full queue."""
    pass


class Queue:
    """
    A basic FIFO queue implementation with optional maximum size.
    """

    def __init__(self, max_size: Optional[int] = None):
        """
        Initialize an empty queue.

        Args:
            max_size: Optional maximum capacity

        Raises:
            ValueError: If max_size is not positive
        """
        if max_size is not None and max_size <= 0:
            raise ValueError("max_size must be positive")
        self._items: List[Any] = []
        self._max_size = max_size

    def enqueue(self, item: Any) -> None:
        """
        Add an item to the back of the queue.

        Raises:
            QueueFullError: If the queue is at maximum capacity
        """
        if self._max_size is not None and len(self._items) >= self._max_size:
            raise QueueFullError("Queue is full")
        self._items.append(item)

    def dequeue(self) -> Any:
        """
        Remove and return the front item.

        Raises:
            QueueEmptyError: If the queue is empty
        """
        if self.is_empty():
            raise QueueEmptyError("Cannot dequeue from empty queue")
        return self._items.pop(0)

    def peek(self) -> Any:
        """
        Return the front item without removing it.

        Raises:
            QueueEmptyError: If the queue is empty
        """
        if self.is_empty():
            raise QueueEmptyError("Cannot peek at empty queue")
        return self._items[0]

    def is_empty(self) -> bool:
        """Check if the queue is empty."""
        return len(self._items) == 0

    def is_full(self) -> bool:
        """Check if the queue is full."""
        if self._max_size is None:
            return False
        return len(self._items) >= self._max_size

    def size(self) -> int:
        """Return the number of items."""
        return len(self._items)

    def clear(self) -> None:
        """Remove all items."""
        self._items.clear()

    def to_list(self) -> List[Any]:
        """Return a copy of items as a list (front to back)."""
        return self._items.copy()

    def __len__(self) -> int:
        return len(self._items)

    def __repr__(self) -> str:
        return f"Queue({self._items})"

    def __contains__(self, item: Any) -> bool:
        return item in self._items


class CircularQueue:
    """
    A fixed-size circular queue implementation.
    """

    def __init__(self, capacity: int):
        """
        Initialize a circular queue.

        Args:
            capacity: Fixed capacity of the queue

        Raises:
            ValueError: If capacity is not positive
        """
        if not isinstance(capacity, int) or capacity <= 0:
            raise ValueError("Capacity must be a positive integer")
        self._capacity = capacity
        self._items: List[Optional[Any]] = [None] * capacity
        self._front = 0
        self._rear = -1
        self._size = 0

    def enqueue(self, item: Any) -> None:
        """Add an item to the circular queue."""
        if self.is_full():
            raise QueueFullError("Circular queue is full")
        self._rear = (self._rear + 1) % self._capacity
        self._items[self._rear] = item
        self._size += 1

    def dequeue(self) -> Any:
        """Remove and return the front item."""
        if self.is_empty():
            raise QueueEmptyError("Cannot dequeue from empty circular queue")
        item = self._items[self._front]
        self._items[self._front] = None
        self._front = (self._front + 1) % self._capacity
        self._size -= 1
        return item

    def peek(self) -> Any:
        """Return the front item without removing it."""
        if self.is_empty():
            raise QueueEmptyError("Cannot peek at empty circular queue")
        return self._items[self._front]

    def is_empty(self) -> bool:
        return self._size == 0

    def is_full(self) -> bool:
        return self._size == self._capacity

    def size(self) -> int:
        return self._size

    @property
    def capacity(self) -> int:
        return self._capacity

    def __len__(self) -> int:
        return self._size

    def __repr__(self) -> str:
        items = []
        idx = self._front
        for _ in range(self._size):
            items.append(self._items[idx])
            idx = (idx + 1) % self._capacity
        return f"CircularQueue({items})"


class PriorityQueue:
    """
    A min-priority queue using a heap.
    Items with lower priority values are dequeued first.
    """

    def __init__(self):
        """Initialize an empty priority queue."""
        self._heap: List[Tuple[float, int, Any]] = []
        self._counter = 0  # tie-breaker for equal priorities

    def enqueue(self, item: Any, priority: float = 0) -> None:
        """
        Add an item with a given priority.

        Args:
            item: The item to add
            priority: Priority value (lower = higher priority)
        """
        if not isinstance(priority, (int, float)):
            raise TypeError("Priority must be a number")
        heapq.heappush(self._heap, (priority, self._counter, item))
        self._counter += 1

    def dequeue(self) -> Any:
        """
        Remove and return the highest-priority (lowest value) item.

        Raises:
            QueueEmptyError: If the queue is empty
        """
        if self.is_empty():
            raise QueueEmptyError("Cannot dequeue from empty priority queue")
        _, _, item = heapq.heappop(self._heap)
        return item

    def peek(self) -> Any:
        """Return the highest-priority item without removing it."""
        if self.is_empty():
            raise QueueEmptyError("Cannot peek at empty priority queue")
        return self._heap[0][2]

    def is_empty(self) -> bool:
        return len(self._heap) == 0

    def size(self) -> int:
        return len(self._heap)

    def __len__(self) -> int:
        return len(self._heap)

    def __repr__(self) -> str:
        items = [(p, item) for p, _, item in sorted(self._heap)]
        return f"PriorityQueue({items})"
