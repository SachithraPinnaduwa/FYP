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
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b