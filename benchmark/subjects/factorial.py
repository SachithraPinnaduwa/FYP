"""
Factorial module - Subject for test generation benchmarking.
Contains various implementations of factorial and related functions.
"""

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
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def factorial_iterative(n: int) -> int:
    """
    Calculate factorial using iteration instead of recursion.
    
    Args:
        n: A non-negative integer
        
    Returns:
        The factorial of n
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def double_factorial(n: int) -> int:
    """
    Calculate the double factorial of n (n!!).
    n!! = n * (n-2) * (n-4) * ... * 1 (or 2)
    
    Args:
        n: A non-negative integer
        
    Returns:
        The double factorial of n
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Double factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    return n * double_factorial(n - 2)


def falling_factorial(n: int, k: int) -> int:
    """
    Calculate the falling factorial (n)_k = n * (n-1) * ... * (n-k+1).
    
    Args:
        n: The base number
        k: The number of terms
        
    Returns:
        The falling factorial
    """
    if not isinstance(n, int) or not isinstance(k, int):
        raise TypeError("Both inputs must be integers")
    if k < 0:
        raise ValueError("k must be non-negative")
    if k == 0:
        return 1
    
    result = 1
    for i in range(k):
        result *= (n - i)
    return result


def binomial_coefficient(n: int, k: int) -> int:
    """
    Calculate the binomial coefficient C(n, k) = n! / (k! * (n-k)!).
    
    Args:
        n: Total number of items
        k: Number of items to choose
        
    Returns:
        The binomial coefficient
    """
    if not isinstance(n, int) or not isinstance(k, int):
        raise TypeError("Both inputs must be integers")
    if k < 0 or n < 0:
        raise ValueError("Both n and k must be non-negative")
    if k > n:
        return 0
    
    return factorial(n) // (factorial(k) * factorial(n - k))
