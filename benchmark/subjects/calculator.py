"""
Calculator module - Subject for test generation benchmarking.
Contains arithmetic and scientific calculator functionality.
"""

import math
from typing import List, Union

Number = Union[int, float]


class CalculatorError(Exception):
    """Base exception for calculator errors."""
    pass


class DivisionByZeroError(CalculatorError):
    """Exception raised for division by zero."""
    pass


class InvalidOperationError(CalculatorError):
    """Exception raised for invalid mathematical operations."""
    pass


class Calculator:
    """
    A calculator class supporting basic and advanced mathematical operations.
    Maintains a history of calculations.
    """
    
    def __init__(self):
        """Initialize the calculator with empty history."""
        self._history: List[str] = []
        self._last_result: Number = 0
    
    @property
    def last_result(self) -> Number:
        """Get the last calculation result."""
        return self._last_result
    
    @property
    def history(self) -> List[str]:
        """Get a copy of the calculation history."""
        return self._history.copy()
    
    def _record(self, operation: str, result: Number) -> Number:
        """Record an operation in history and store the result."""
        self._history.append(f"{operation} = {result}")
        self._last_result = result
        return result
    
    def clear_history(self) -> None:
        """Clear the calculation history."""
        self._history.clear()
        self._last_result = 0
    
    # Basic arithmetic operations
    
    def add(self, a: Number, b: Number) -> Number:
        """Add two numbers."""
        result = a + b
        return self._record(f"{a} + {b}", result)
    
    def subtract(self, a: Number, b: Number) -> Number:
        """Subtract b from a."""
        result = a - b
        return self._record(f"{a} - {b}", result)
    
    def multiply(self, a: Number, b: Number) -> Number:
        """Multiply two numbers."""
        result = a * b
        return self._record(f"{a} * {b}", result)
    
    def divide(self, a: Number, b: Number) -> float:
        """
        Divide a by b.
        
        Raises:
            DivisionByZeroError: If b is zero
        """
        if b == 0:
            raise DivisionByZeroError("Cannot divide by zero")
        result = a / b
        return self._record(f"{a} / {b}", result)
    
    def floor_divide(self, a: Number, b: Number) -> int:
        """
        Perform floor division of a by b.
        
        Raises:
            DivisionByZeroError: If b is zero
        """
        if b == 0:
            raise DivisionByZeroError("Cannot divide by zero")
        result = a // b
        return self._record(f"{a} // {b}", result)
    
    def modulo(self, a: Number, b: Number) -> Number:
        """
        Calculate a modulo b.
        
        Raises:
            DivisionByZeroError: If b is zero
        """
        if b == 0:
            raise DivisionByZeroError("Cannot calculate modulo with zero")
        result = a % b
        return self._record(f"{a} % {b}", result)
    
    def power(self, base: Number, exponent: Number) -> Number:
        """
        Calculate base raised to the power of exponent.
        
        Raises:
            InvalidOperationError: For invalid power operations
        """
        try:
            result = base ** exponent
            return self._record(f"{base} ^ {exponent}", result)
        except (ValueError, OverflowError) as e:
            raise InvalidOperationError(f"Invalid power operation: {e}")
    
    # Advanced mathematical operations
    
    def square_root(self, n: Number) -> float:
        """
        Calculate the square root of n.
        
        Raises:
            InvalidOperationError: If n is negative
        """
        if n < 0:
            raise InvalidOperationError("Cannot calculate square root of negative number")
        result = math.sqrt(n)
        return self._record(f"sqrt({n})", result)
    
    def absolute(self, n: Number) -> Number:
        """Calculate the absolute value of n."""
        result = abs(n)
        return self._record(f"|{n}|", result)
    
    def factorial(self, n: int) -> int:
        """
        Calculate the factorial of n.
        
        Raises:
            InvalidOperationError: If n is negative or not an integer
        """
        if not isinstance(n, int):
            raise InvalidOperationError("Factorial requires an integer")
        if n < 0:
            raise InvalidOperationError("Factorial is not defined for negative numbers")
        result = math.factorial(n)
        return self._record(f"{n}!", result)
    
    def log(self, n: Number, base: Number = math.e) -> float:
        """
        Calculate the logarithm of n with the given base.
        
        Args:
            n: The number to take the log of
            base: The base of the logarithm (default: e)
            
        Raises:
            InvalidOperationError: If n <= 0 or base <= 0
        """
        if n <= 0:
            raise InvalidOperationError("Logarithm requires a positive number")
        if base <= 0 or base == 1:
            raise InvalidOperationError("Logarithm base must be positive and not 1")
        result = math.log(n, base)
        return self._record(f"log_{base}({n})", result)
    
    def log10(self, n: Number) -> float:
        """Calculate the base-10 logarithm of n."""
        if n <= 0:
            raise InvalidOperationError("Logarithm requires a positive number")
        result = math.log10(n)
        return self._record(f"log10({n})", result)
    
    # Trigonometric functions
    
    def sin(self, angle: Number) -> float:
        """Calculate the sine of angle (in radians)."""
        result = math.sin(angle)
        return self._record(f"sin({angle})", result)
    
    def cos(self, angle: Number) -> float:
        """Calculate the cosine of angle (in radians)."""
        result = math.cos(angle)
        return self._record(f"cos({angle})", result)
    
    def tan(self, angle: Number) -> float:
        """Calculate the tangent of angle (in radians)."""
        result = math.tan(angle)
        return self._record(f"tan({angle})", result)
    
    # Statistical operations on lists
    
    def sum_list(self, numbers: List[Number]) -> Number:
        """Calculate the sum of a list of numbers."""
        if not numbers:
            raise InvalidOperationError("Cannot sum empty list")
        result = sum(numbers)
        return self._record(f"sum({numbers})", result)
    
    def average(self, numbers: List[Number]) -> float:
        """Calculate the average of a list of numbers."""
        if not numbers:
            raise InvalidOperationError("Cannot calculate average of empty list")
        result = sum(numbers) / len(numbers)
        return self._record(f"avg({numbers})", result)
    
    def max_value(self, numbers: List[Number]) -> Number:
        """Find the maximum value in a list of numbers."""
        if not numbers:
            raise InvalidOperationError("Cannot find max of empty list")
        result = max(numbers)
        return self._record(f"max({numbers})", result)
    
    def min_value(self, numbers: List[Number]) -> Number:
        """Find the minimum value in a list of numbers."""
        if not numbers:
            raise InvalidOperationError("Cannot find min of empty list")
        result = min(numbers)
        return self._record(f"min({numbers})", result)


def evaluate_expression(expression: str) -> Number:
    """
    Safely evaluate a simple mathematical expression.
    
    Supports: +, -, *, /, parentheses, and numbers
    
    Args:
        expression: A mathematical expression string
        
    Returns:
        The result of the expression
        
    Raises:
        InvalidOperationError: If expression is invalid
    """
    # Remove whitespace
    expression = expression.replace(" ", "")
    
    # Validate characters
    allowed = set("0123456789+-*/().")
    if not all(c in allowed for c in expression):
        raise InvalidOperationError("Expression contains invalid characters")
    
    try:
        # Use ast.literal_eval for safety is not possible for expressions
        # So we carefully validate and use eval
        result = eval(expression, {"__builtins__": {}}, {})
        return result
    except ZeroDivisionError:
        raise DivisionByZeroError("Division by zero in expression")
    except Exception as e:
        raise InvalidOperationError(f"Invalid expression: {e}")
