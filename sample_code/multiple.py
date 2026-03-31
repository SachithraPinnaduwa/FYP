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

