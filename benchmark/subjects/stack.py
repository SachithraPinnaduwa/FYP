"""
Stack module - Subject for test generation benchmarking.
Contains Stack data structure implementation with various operations.
"""

from typing import Any, List, Optional


class StackEmptyError(Exception):
    """Exception raised when trying to pop or peek from an empty stack."""
    pass


class StackOverflowError(Exception):
    """Exception raised when pushing to a full stack."""
    pass


class Stack:
    """
    A stack data structure implementation with optional maximum size.
    
    Attributes:
        max_size: Maximum number of elements (None for unlimited)
    """
    
    def __init__(self, max_size: Optional[int] = None):
        """
        Initialize an empty stack.
        
        Args:
            max_size: Optional maximum size of the stack
        """
        if max_size is not None and max_size <= 0:
            raise ValueError("max_size must be positive")
        self._items: List[Any] = []
        self._max_size = max_size
    
    def push(self, item: Any) -> None:
        """
        Push an item onto the stack.
        
        Args:
            item: The item to push
            
        Raises:
            StackOverflowError: If stack is at maximum capacity
        """
        if self._max_size is not None and len(self._items) >= self._max_size:
            raise StackOverflowError("Stack is full")
        self._items.append(item)
    
    def pop(self) -> Any:
        """
        Remove and return the top item from the stack.
        
        Returns:
            The top item
            
        Raises:
            StackEmptyError: If stack is empty
        """
        if self.is_empty():
            raise StackEmptyError("Cannot pop from empty stack")
        return self._items.pop()
    
    def peek(self) -> Any:
        """
        Return the top item without removing it.
        
        Returns:
            The top item
            
        Raises:
            StackEmptyError: If stack is empty
        """
        if self.is_empty():
            raise StackEmptyError("Cannot peek at empty stack")
        return self._items[-1]
    
    def is_empty(self) -> bool:
        """Check if the stack is empty."""
        return len(self._items) == 0
    
    def is_full(self) -> bool:
        """Check if the stack is full."""
        if self._max_size is None:
            return False
        return len(self._items) >= self._max_size
    
    def size(self) -> int:
        """Return the number of items in the stack."""
        return len(self._items)
    
    def clear(self) -> None:
        """Remove all items from the stack."""
        self._items.clear()
    
    def to_list(self) -> List[Any]:
        """Return a copy of the stack as a list (bottom to top)."""
        return self._items.copy()
    
    def __len__(self) -> int:
        """Return the number of items in the stack."""
        return len(self._items)
    
    def __repr__(self) -> str:
        """Return a string representation of the stack."""
        return f"Stack({self._items})"
    
    def __contains__(self, item: Any) -> bool:
        """Check if an item is in the stack."""
        return item in self._items


class MinStack(Stack):
    """
    A stack that supports O(1) retrieval of the minimum element.
    """
    
    def __init__(self, max_size: Optional[int] = None):
        super().__init__(max_size)
        self._min_stack: List[Any] = []
    
    def push(self, item: Any) -> None:
        """Push an item and update the minimum tracking."""
        super().push(item)
        if not self._min_stack or item <= self._min_stack[-1]:
            self._min_stack.append(item)
    
    def pop(self) -> Any:
        """Pop an item and update the minimum tracking."""
        item = super().pop()
        if item == self._min_stack[-1]:
            self._min_stack.pop()
        return item
    
    def get_min(self) -> Any:
        """
        Get the minimum element in the stack.
        
        Returns:
            The minimum element
            
        Raises:
            StackEmptyError: If stack is empty
        """
        if self.is_empty():
            raise StackEmptyError("Cannot get min from empty stack")
        return self._min_stack[-1]
    
    def clear(self) -> None:
        """Clear both the main stack and min tracking stack."""
        super().clear()
        self._min_stack.clear()
