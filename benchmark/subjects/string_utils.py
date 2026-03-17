"""
String Utilities module - Subject for test generation benchmarking.
Contains various string manipulation functions.
"""

from typing import List, Optional


def reverse_string(s: str) -> str:
    """
    Reverse a string.

    Args:
        s: The input string

    Returns:
        The reversed string

    Raises:
        TypeError: If input is not a string
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    return s[::-1]


def is_palindrome(s: str) -> bool:
    """
    Check if a string is a palindrome (case-insensitive, ignoring spaces).

    Args:
        s: The input string

    Returns:
        True if the string is a palindrome
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]


def count_vowels(s: str) -> int:
    """
    Count the number of vowels in a string.

    Args:
        s: The input string

    Returns:
        The number of vowels
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    return sum(1 for c in s.lower() if c in 'aeiou')


def caesar_cipher(text: str, shift: int) -> str:
    """
    Apply Caesar cipher encryption to text.

    Args:
        text: The text to encrypt
        shift: The number of positions to shift

    Returns:
        The encrypted text
    """
    if not isinstance(text, str):
        raise TypeError("Text must be a string")
    if not isinstance(shift, int):
        raise TypeError("Shift must be an integer")

    result = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26 + base
            result.append(chr(shifted))
        else:
            result.append(char)
    return ''.join(result)


def word_frequency(text: str) -> dict:
    """
    Count the frequency of each word in a text.

    Args:
        text: The input text

    Returns:
        Dictionary mapping words to their frequencies
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    if not text.strip():
        return {}
    words = text.lower().split()
    freq = {}
    for word in words:
        cleaned = ''.join(c for c in word if c.isalnum())
        if cleaned:
            freq[cleaned] = freq.get(cleaned, 0) + 1
    return freq


def longest_common_prefix(strings: List[str]) -> str:
    """
    Find the longest common prefix among a list of strings.

    Args:
        strings: List of strings

    Returns:
        The longest common prefix

    Raises:
        TypeError: If input is not a list of strings
    """
    if not isinstance(strings, list):
        raise TypeError("Input must be a list")
    if not strings:
        return ""
    if not all(isinstance(s, str) for s in strings):
        raise TypeError("All elements must be strings")

    prefix = strings[0]
    for s in strings[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix


def is_anagram(s1: str, s2: str) -> bool:
    """
    Check if two strings are anagrams of each other.

    Args:
        s1: First string
        s2: Second string

    Returns:
        True if the strings are anagrams
    """
    if not isinstance(s1, str) or not isinstance(s2, str):
        raise TypeError("Both inputs must be strings")
    return sorted(s1.lower().replace(" ", "")) == sorted(s2.lower().replace(" ", ""))


def truncate(text: str, max_length: int, suffix: str = "...") -> str:
    """
    Truncate a string to a maximum length, adding a suffix if truncated.

    Args:
        text: The input text
        max_length: Maximum length of the result
        suffix: Suffix to add if truncated

    Returns:
        The truncated string

    Raises:
        ValueError: If max_length is less than the length of suffix
    """
    if not isinstance(text, str):
        raise TypeError("Text must be a string")
    if max_length < len(suffix):
        raise ValueError("max_length must be at least the length of suffix")
    if len(text) <= max_length:
        return text
    return text[:max_length - len(suffix)] + suffix
