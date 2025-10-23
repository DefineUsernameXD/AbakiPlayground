"""
Simple Calculator with Intentional Bugs
This calculator has several errors that need to be fixed!
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
    """Divide a by b
    Handle division by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def power(a, b):
    """Raise a to the power of b"""
    return a ** b

def main():
    print("Welcome to the Buggy Calculator!")
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
    
    # Test division
    try:
        result = divide(10, 0)
        print(f"10 / 0 = {result}")
    except ValueError as e:
        print(e)
    
    # Test power
    result = power(3, 2)
    print(f"3 ^ 2 = {result}")
    
    # Corrected variable name
    count = 5
    print(f"Total calculations: {count}")
    
    print("=" * 40)
    print("Calculations complete!")

if __name__ == "__main__":
    main()