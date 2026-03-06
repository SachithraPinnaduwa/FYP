"""
Temperature Converter module - Subject for test generation benchmarking.
Contains temperature conversion and weather-related utility functions.
"""

from typing import Dict, List, Optional, Tuple


class TemperatureError(Exception):
    """Base exception for temperature errors."""
    pass


class AbsoluteZeroError(TemperatureError):
    """Raised when a temperature is below absolute zero."""
    pass


# Absolute zero constants
ABSOLUTE_ZERO_C = -273.15
ABSOLUTE_ZERO_F = -459.67
ABSOLUTE_ZERO_K = 0.0


def celsius_to_fahrenheit(celsius: float) -> float:
    """
    Convert Celsius to Fahrenheit.

    Args:
        celsius: Temperature in Celsius

    Returns:
        Temperature in Fahrenheit

    Raises:
        TypeError: If input is not a number
        AbsoluteZeroError: If temperature is below absolute zero
    """
    if not isinstance(celsius, (int, float)):
        raise TypeError("Temperature must be a number")
    if celsius < ABSOLUTE_ZERO_C:
        raise AbsoluteZeroError(
            f"{celsius}°C is below absolute zero ({ABSOLUTE_ZERO_C}°C)"
        )
    return round(celsius * 9 / 5 + 32, 2)


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """
    Convert Fahrenheit to Celsius.

    Raises:
        TypeError: If input is not a number
        AbsoluteZeroError: If temperature is below absolute zero
    """
    if not isinstance(fahrenheit, (int, float)):
        raise TypeError("Temperature must be a number")
    if fahrenheit < ABSOLUTE_ZERO_F:
        raise AbsoluteZeroError(
            f"{fahrenheit}°F is below absolute zero ({ABSOLUTE_ZERO_F}°F)"
        )
    return round((fahrenheit - 32) * 5 / 9, 2)


def celsius_to_kelvin(celsius: float) -> float:
    """
    Convert Celsius to Kelvin.

    Raises:
        AbsoluteZeroError: If temperature is below absolute zero
    """
    if not isinstance(celsius, (int, float)):
        raise TypeError("Temperature must be a number")
    if celsius < ABSOLUTE_ZERO_C:
        raise AbsoluteZeroError(
            f"{celsius}°C is below absolute zero ({ABSOLUTE_ZERO_C}°C)"
        )
    return round(celsius + 273.15, 2)


def kelvin_to_celsius(kelvin: float) -> float:
    """
    Convert Kelvin to Celsius.

    Raises:
        AbsoluteZeroError: If temperature is below absolute zero
    """
    if not isinstance(kelvin, (int, float)):
        raise TypeError("Temperature must be a number")
    if kelvin < ABSOLUTE_ZERO_K:
        raise AbsoluteZeroError(f"{kelvin}K is below absolute zero (0K)")
    return round(kelvin - 273.15, 2)


def fahrenheit_to_kelvin(fahrenheit: float) -> float:
    """Convert Fahrenheit to Kelvin."""
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)


def kelvin_to_fahrenheit(kelvin: float) -> float:
    """Convert Kelvin to Fahrenheit."""
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)


def convert_temperature(
    value: float, from_unit: str, to_unit: str
) -> float:
    """
    Convert temperature between any two units.

    Args:
        value: The temperature value
        from_unit: Source unit ('C', 'F', or 'K')
        to_unit: Target unit ('C', 'F', or 'K')

    Returns:
        Converted temperature

    Raises:
        ValueError: If units are invalid
    """
    valid_units = {'C', 'F', 'K'}
    from_unit = from_unit.upper()
    to_unit = to_unit.upper()
    if from_unit not in valid_units:
        raise ValueError(f"Invalid source unit: {from_unit}. Must be C, F, or K")
    if to_unit not in valid_units:
        raise ValueError(f"Invalid target unit: {to_unit}. Must be C, F, or K")

    if from_unit == to_unit:
        return float(value)

    converters = {
        ('C', 'F'): celsius_to_fahrenheit,
        ('C', 'K'): celsius_to_kelvin,
        ('F', 'C'): fahrenheit_to_celsius,
        ('F', 'K'): fahrenheit_to_kelvin,
        ('K', 'C'): kelvin_to_celsius,
        ('K', 'F'): kelvin_to_fahrenheit,
    }
    return converters[(from_unit, to_unit)](value)


def classify_temperature(celsius: float) -> str:
    """
    Classify a temperature in Celsius into a category.

    Returns:
        One of: 'freezing', 'cold', 'cool', 'comfortable', 'warm', 'hot', 'extreme'
    """
    if not isinstance(celsius, (int, float)):
        raise TypeError("Temperature must be a number")
    if celsius < ABSOLUTE_ZERO_C:
        raise AbsoluteZeroError("Below absolute zero")

    if celsius <= 0:
        return "freezing"
    elif celsius <= 10:
        return "cold"
    elif celsius <= 18:
        return "cool"
    elif celsius <= 25:
        return "comfortable"
    elif celsius <= 32:
        return "warm"
    elif celsius <= 40:
        return "hot"
    else:
        return "extreme"


def batch_convert(
    temperatures: List[float], from_unit: str, to_unit: str
) -> List[float]:
    """
    Convert a list of temperatures.

    Args:
        temperatures: List of temperature values
        from_unit: Source unit
        to_unit: Target unit

    Returns:
        List of converted temperatures
    """
    if not isinstance(temperatures, list):
        raise TypeError("Temperatures must be a list")
    return [convert_temperature(t, from_unit, to_unit) for t in temperatures]


def temperature_stats(temperatures: List[float]) -> Dict[str, float]:
    """
    Compute statistics for a list of temperatures.

    Args:
        temperatures: List of temperatures

    Returns:
        Dictionary with min, max, mean, and range

    Raises:
        ValueError: If the list is empty
    """
    if not isinstance(temperatures, list):
        raise TypeError("Input must be a list")
    if not temperatures:
        raise ValueError("Temperature list cannot be empty")
    if not all(isinstance(t, (int, float)) for t in temperatures):
        raise TypeError("All temperatures must be numbers")

    return {
        "min": round(min(temperatures), 2),
        "max": round(max(temperatures), 2),
        "mean": round(sum(temperatures) / len(temperatures), 2),
        "range": round(max(temperatures) - min(temperatures), 2),
    }
