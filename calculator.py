"""
Simple Calculator

This module implements basic arithmetic operations with clear docstrings
and a small test harness in main(). Division by zero is handled by raising
ValueError, which the caller can catch and report.
"""

def add(a, b):
    """Add two numbers and return the sum."""
    return a + b

def subtract(a, b):
    """Subtract b from a and return the difference."""
    return a - b

def multiply(a, b):
    """Multiply two numbers and return the product."""
    return a * b

def divide(a, b):
    """Divide a by b and return the quotient.

    Raises
    ------
    ValueError
        If b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def power(a, b):
    """Raise a to the power of b and return the result."""
    return a ** b

def main():
    print("Welcome to the Calculator!")
    print("=" * 40)
    
    count = 0  # number of calculations attempted

    # Test addition
    result = add(10, 5)
    print(f"10 + 5 = {result}")
    count += 1
    
    # Test subtraction
    result = subtract(10, 5)
    print(f"10 - 5 = {result}")
    count += 1
    
    # Test multiplication
    result = multiply(10, 5)
    print(f"10 * 5 = {result}")
    count += 1
    
    # Test division (handle division by zero)
    try:
        result = divide(10, 0)
        print(f"10 / 0 = {result}")
    except ValueError as e:
        print(f"10 / 0 error: {e}")
    finally:
        count += 1
    
    # Test power (2 ** 3)
    result = power(2, 3)
    print(f"2 ** 3 = {result}")
    count += 1
    
    print(f"Total calculations: {count}")
    
    print("=" * 40)
    print("Calculations complete!")

if __name__ == "__main__":
    main()
