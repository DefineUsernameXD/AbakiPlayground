"""
Simple Calculator
A tiny calculator with basic operations.
"""

def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract b from a"""
    return a - b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def divide(a, b):
    """Divide a by b; handle divide-by-zero by returning None."""
    if b == 0:
        return None
    return a / b

def power(a, b):
    """Raise a to the power of b"""
    return a ** b

def main():
    print("Welcome to the Calculator!")
    print("=" * 40)

    # Test addition
    result = add(10, 5)
    print(f"10 + 5 = {result}")

    # Test subtraction
    result = subtract(10, 5)
    print(f"10 - 5 = {result}")

    # Test multiplication
    result = multiply(10, 5)
    print(f"10 * 5 = {result}")

    # Test division (handle divide by zero)
    result = divide(10, 0)
    if result is None:
        print("10 / 0 = undefined (division by zero)")
    else:
        print(f"10 / 0 = {result}")

    # Test power (correct args and label)
    result = power(2, 3)
    print(f"2 ^ 3 = {result}")

    # Count of calculations printed above
    count = 5
    print(f"Total calculations: {count}")

    print("=" * 40)
    print("Calculations complete!")

if __name__ == "__main__":
    main()