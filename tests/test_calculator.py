"""
Unit tests for the calculator module.

These tests demonstrate:
- Basic pytest usage
- Test parametrization
- Exception testing
- Test organization
"""

import pytest
from src.calculator import add, subtract, multiply, divide


class TestAdd:
    """Tests for the add function."""
    
    def test_add_positive_numbers(self):
        """Test adding two positive numbers."""
        assert add(2, 3) == 5
    
    def test_add_negative_numbers(self):
        """Test adding two negative numbers."""
        assert add(-2, -3) == -5
    
    def test_add_mixed_numbers(self):
        """Test adding positive and negative numbers."""
        assert add(5, -3) == 2
    
    def test_add_with_zero(self):
        """Test adding with zero."""
        assert add(5, 0) == 5
        assert add(0, 5) == 5
    
    def test_add_floats(self):
        """Test adding floating point numbers."""
        assert add(2.5, 3.7) == pytest.approx(6.2)


class TestSubtract:
    """Tests for the subtract function."""
    
    def test_subtract_positive_numbers(self):
        """Test subtracting two positive numbers."""
        assert subtract(5, 3) == 2
    
    def test_subtract_negative_numbers(self):
        """Test subtracting two negative numbers."""
        assert subtract(-5, -3) == -2
    
    def test_subtract_with_zero(self):
        """Test subtracting with zero."""
        assert subtract(5, 0) == 5
        assert subtract(0, 5) == -5


class TestMultiply:
    """Tests for the multiply function."""
    
    def test_multiply_positive_numbers(self):
        """Test multiplying two positive numbers."""
        assert multiply(4, 3) == 12
    
    def test_multiply_by_zero(self):
        """Test multiplying by zero."""
        assert multiply(5, 0) == 0
        assert multiply(0, 5) == 0
    
    def test_multiply_negative_numbers(self):
        """Test multiplying negative numbers."""
        assert multiply(-2, 3) == -6
        assert multiply(-2, -3) == 6
    
    def test_multiply_floats(self):
        """Test multiplying floating point numbers."""
        assert multiply(2.5, 4) == pytest.approx(10.0)


class TestDivide:
    """Tests for the divide function."""
    
    def test_divide_positive_numbers(self):
        """Test dividing two positive numbers."""
        assert divide(10, 2) == 5.0
    
    def test_divide_with_remainder(self):
        """Test division with remainder."""
        assert divide(7, 2) == pytest.approx(3.5)
    
    def test_divide_negative_numbers(self):
        """Test dividing negative numbers."""
        assert divide(-10, 2) == -5.0
        assert divide(10, -2) == -5.0
        assert divide(-10, -2) == 5.0
    
    def test_divide_by_zero_raises_error(self):
        """Test that dividing by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(10, 0)
    
    def test_divide_zero_by_number(self):
        """Test dividing zero by a number."""
        assert divide(0, 5) == 0.0


# Parametrized tests example
@pytest.mark.parametrize("a,b,expected", [
    (1, 1, 2),
    (10, 20, 30),
    (-5, 5, 0),
    (0, 0, 0),
    (100, -50, 50),
])
def test_add_parametrized(a, b, expected):
    """Test add function with multiple parameter sets."""
    assert add(a, b) == expected


@pytest.mark.parametrize("a,b,expected", [
    (10, 5, 2.0),
    (100, 10, 10.0),
    (7, 2, 3.5),
    (-10, 5, -2.0),
])
def test_divide_parametrized(a, b, expected):
    """Test divide function with multiple parameter sets."""
    assert divide(a, b) == pytest.approx(expected)
