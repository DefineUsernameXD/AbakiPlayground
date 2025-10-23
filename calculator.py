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
    if b == 0:
        print("Cannot multiply by zero")
        return None
    return a * b
    # Test multiplication with zero
    result = multiply(10, 0)
    if result is not None:
        print(f"10 * 0 = {result}")
    else:
        print("Cannot multiply by zero")
    return a * b

def divide(a, b):
    """Divide a by b
    Handles division by zero by returning None."""
    if b == 0:
        print("Division by zero")
        return None
    return a / b
def power(a, b):
    """Raise a to the power of b
    Handles negative exponents"""
    return a ** b if b >= 0 else None
    """Raise a to the power of b"""
    return a ** b

    # Test power with negative exponent
    result = power(2, -3)
    print(f"2 ^ -3 = {result}")
def main():
    print("Welcome to the Buggy Calculator!")
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
    
    # Test division
    result = divide(10, 0)
    if result is None:
        print("Division by zero")
    else:
        print(f"10 / 0 = {result}")
    
    # Test power
    result = power(2, 3)
    print(f"2 ^ 3 = {result}")
    
    count = 6
    print(f"Total calculations: {count}")
    # Test addition
    result = add(10, 5)
    print(f"10 + 5 = {result}")
    
    # Test subtraction
    result = subtract(10, 5)
    print(f"10 - 5 = {result}")
    
    # Test multiplication
    
    # Test division
    result = divide(10, 0)
    if result is None:
        print("Division by zero")
    else:
        print(f"10 / 0 = {result}")
    
    # Test power
    result = power(2, 3)
    print(f"2 ^ 3 = {result}")
    
    count = 5
    print(f"Total calculations: {count}")
    
    print("=" * 40)
    print("Calculations complete!")

if __name__ == "__main__":
    main()
