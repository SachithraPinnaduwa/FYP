"""
Sample Python Module for Test Generation Demo

This module contains various functions and classes that demonstrate
different testing scenarios including:
- Basic arithmetic operations
- Edge cases (division by zero, empty inputs)
- Data structures (stack, queue-like behavior)
- String manipulation
- Error handling

Use this file to test the AI-powered unit test generator.
"""

from typing import List, Optional, Union


def divide(a: float, b: float) -> float:
    """
    Divide two numbers.
    
    Args:
        a: The dividend
        b: The divisor
        
    Returns:
        The quotient of a divided by b
        
    Raises:
        ZeroDivisionError: If b is zero
        
    Example:
        >>> divide(10, 2)
        5.0
        >>> divide(7, 3)
        2.333...
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


def factorial(n: int) -> int:
    """
    Calculate the factorial of a non-negative integer.
    
    Args:
        n: A non-negative integer
        
    Returns:
        The factorial of n (n!)
        
    Raises:
        ValueError: If n is negative
        TypeError: If n is not an integer
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def find_max(numbers: List[Union[int, float]]) -> Union[int, float]:
    """
    Find the maximum value in a list of numbers.
    
    Args:
        numbers: A non-empty list of numbers
        
    Returns:
        The maximum value in the list
        
    Raises:
        ValueError: If the list is empty
    """
    if not numbers:
        raise ValueError("Cannot find max of empty list")
    return max(numbers)


def is_palindrome(s: str) -> bool:
    """
    Check if a string is a palindrome (ignoring case and spaces).
    
    Args:
        s: The string to check
        
    Returns:
        True if the string is a palindrome, False otherwise
        
    Example:
        >>> is_palindrome("A man a plan a canal Panama")
        True
        >>> is_palindrome("hello")
        False
    """
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]


class Stack:
    """
    A simple stack implementation using a list.
    
    Supports push, pop, peek, and size operations.
    """
    
    def __init__(self, max_size: Optional[int] = None):
        """
        Initialize an empty stack.
        
        Args:
            max_size: Optional maximum size limit for the stack
        """
        self._items: List = []
        self._max_size = max_size
    
    def push(self, item) -> None:
        """
        Push an item onto the stack.
        
        Args:
            item: The item to push
            
        Raises:
            OverflowError: If stack is at max capacity
        """
        if self._max_size is not None and len(self._items) >= self._max_size:
            raise OverflowError("Stack is full")
        self._items.append(item)
    
    def pop(self):
        """
        Remove and return the top item from the stack.
        
        Returns:
            The top item
            
        Raises:
            IndexError: If the stack is empty
        """
        if not self._items:
            raise IndexError("Pop from empty stack")
        return self._items.pop()
    
    def peek(self):
        """
        Return the top item without removing it.
        
        Returns:
            The top item
            
        Raises:
            IndexError: If the stack is empty
        """
        if not self._items:
            raise IndexError("Peek at empty stack")
        return self._items[-1]
    
    def is_empty(self) -> bool:
        """Check if the stack is empty."""
        return len(self._items) == 0
    
    def size(self) -> int:
        """Return the number of items in the stack."""
        return len(self._items)


class Calculator:
    """
    A calculator class with basic arithmetic operations and memory.
    """
    
    def __init__(self):
        """Initialize calculator with memory set to 0."""
        self.memory: float = 0.0
    
    def add(self, a: float, b: float) -> float:
        """Add two numbers."""
        return a + b
    
    def subtract(self, a: float, b: float) -> float:
        """Subtract b from a."""
        return a - b
    
    def multiply(self, a: float, b: float) -> float:
        """Multiply two numbers."""
        return a * b
    
    def divide(self, a: float, b: float) -> float:
        """Divide a by b. Raises ZeroDivisionError if b is 0."""
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b
    
    def store(self, value: float) -> None:
        """Store a value in memory."""
        self.memory = value
    
    def recall(self) -> float:
        """Recall the value from memory."""
        return self.memory
    
    def clear_memory(self) -> None:
        """Clear the memory (set to 0)."""
        self.memory = 0.0


def fizzbuzz(n: int) -> List[str]:
    """
    Generate FizzBuzz sequence from 1 to n.
    
    Args:
        n: The upper limit (inclusive)
        
    Returns:
        List of strings where:
        - "FizzBuzz" for multiples of both 3 and 5
        - "Fizz" for multiples of 3
        - "Buzz" for multiples of 5
        - The number as string otherwise
        
    Raises:
        ValueError: If n is less than 1
    """
    if n < 1:
        raise ValueError("n must be at least 1")
    
    result = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result


if __name__ == "__main__":
    # Quick demo
    print("divide(10, 2) =", divide(10, 2))
    print("factorial(5) =", factorial(5))
    print("is_palindrome('racecar') =", is_palindrome("racecar"))
    print("fizzbuzz(15) =", fizzbuzz(15))
    
    stack = Stack()
    stack.push(1)
    stack.push(2)
    print("Stack peek:", stack.peek())
    print("Stack pop:", stack.pop())
