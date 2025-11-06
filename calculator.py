"""
Simple Calculator
This calculator performs basic arithmetic operations.
"""

def add(a, b):
    """Add two numbers."""
    return a + b

def subtract(a, b):
    """Subtract b from a."""
    return a - b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def divide(a, b):
    """Divide a by b, handling division by zero."""
    if b == 0:
        return "Cannot divide by zero!"
    return a / b

def power(a, b):
    """Raise a to the power of b."""
    return a ** b

def main():
    print("Welcome to the Calculator!")
    print("=" * 40)
    
    count = 0  # Initialize calculation count
    
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
    
    # Test division
    result = divide(10, 0)
    print(f"10 / 0 = {result}")
    count += 1
    
    # Test power
    result = power(2, 3)
    print(f"2 ** 3 = {result}")
    count += 1
    
    print(f"Total calculations: {count}")
    
    print("=" * 40)
    print("Calculations complete!")

if __name__ == "__main__":
    main()