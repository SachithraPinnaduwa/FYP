"""sample_code package

Expose useful utilities for tests and demos.
"""
from .sample_code import (
    divide,
    factorial,
    find_max,
    is_palindrome,
    Stack,
    Calculator,
    fizzbuzz,
)

from .realistic_service import (
    CSVDataProcessor,
    summarize_csv,
    DataProcessingError,
)

__all__ = [
    "divide",
    "factorial",
    "find_max",
    "is_palindrome",
    "Stack",
    "Calculator",
    "fizzbuzz",
    "CSVDataProcessor",
    "summarize_csv",
    "DataProcessingError",
]
