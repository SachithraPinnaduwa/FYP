"""
negative_cases/prose_at_bottom.py
Expected error: "The input contains non-Python text. Detected prose-like content at: ..."

Valid Python code at the top, but random descriptive text appended at the
bottom (as if someone copy-pasted a README excerpt after the code).
"""

def celsius_to_fahrenheit(c: float) -> float:
    """Convert Celsius to Fahrenheit."""
    return c * 9 / 5 + 32


def fahrenheit_to_celsius(f: float) -> float:
    """Convert Fahrenheit to Celsius."""
    return (f - 32) * 5 / 9


The above functions convert temperatures between Celsius and Fahrenheit scales
These are standard conversion formulas used in everyday scientific applications
Please make sure to pass numeric values otherwise the function will raise an error
