"""
A simple calculator module with basic arithmetic operations.

This module is designed to demonstrate:
- Simple Python functions
- Type hints
- Docstrings
- Error handling
"""


def add(a: float, b: float) -> float:
    """
    Add two numbers together.
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        The sum of a and b
    
    Example:
        >>> add(2, 3)
        5
    """
    return a + b


def subtract(a: float, b: float) -> float:
    """
    Subtract b from a.
    
    Args:
        a: First number
        b: Number to subtract
    
    Returns:
        The difference of a and b
    
    Example:
        >>> subtract(5, 3)
        2
    """
    return a - b


def multiply(a: float, b: float) -> float:
    """
    Multiply two numbers.
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        The product of a and b
    
    Example:
        >>> multiply(4, 3)
        12
    """
    return a * b


def divide(a: float, b: float) -> float:
    """
    Divide a by b.
    
    Args:
        a: Numerator
        b: Denominator
    
    Returns:
        The quotient of a divided by b
    
    Raises:
        ValueError: If b is zero
    
    Example:
        >>> divide(10, 2)
        5.0
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
