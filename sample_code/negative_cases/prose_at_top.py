"""
negative_cases/prose_at_top.py
Expected error: "The input appears to contain non-Python text..." (syntax error path)
  OR "The input contains non-Python text..." (prose scanner path)

A block of natural language description appears at the very top of the
file before any Python code, causing either a parse failure or a prose
detection hit.
"""

This module provides utility functions for string manipulation
It includes methods for reversing strings and checking palindromes
These functions are useful in text processing tasks


def reverse_string(s: str) -> str:
    """Reverse a string."""
    return s[::-1]


def is_palindrome(s: str) -> str:
    """Check whether a string is a palindrome."""
    cleaned = s.lower().replace(" ", "")
    return cleaned == cleaned[::-1]
