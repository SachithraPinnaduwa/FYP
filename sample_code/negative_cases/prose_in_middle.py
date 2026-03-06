"""
negative_cases/prose_in_middle.py
Expected error: "The input contains non-Python text. Detected prose-like content at: ..."

This file starts and ends with valid Python code but has a block of
plain English text inserted between two functions.
"""

def multiply(a, b):
    """Return the product of a and b."""
    return a * b


This function multiplies two numbers together and returns the result
It is commonly used in mathematical computations and scientific applications
You should call this when you need to find the product of two values


def divide(a, b):
    """Return the quotient of a divided by b."""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b
