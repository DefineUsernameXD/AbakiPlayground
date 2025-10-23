"""
Simple Calculator with Intentional Bugs
This calculator has several errors that need to be fixed!
"""

def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract b from a"""
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
    Handles division by zero by returning None."""
    if b == 0:
        return None
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
    
    # Test multiplication - Corrected function called
    result = multiply(10, 5)
    print(f"10 * 5 = {result}")
    
    # Test division - Division by zero handled
    result = divide(10, 0)
    if result is None:
        print("Division by zero")
    else:
        print(f"10 / 0 = {result}")
    
    # Test power - Correct order of arguments
    result = power(2, 3)
    print(f"2 ^ 3 = {result}")
    
    # Define undefined variable
    count = 5
    print(f"Total calculations: {count}")
    
    print("=" * 40)
    print("Calculations complete!")

def subtract(a, b):
    """Subtract b from a"""
    return a - b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def divide(a, b):
    """Divide a by b
    Handles division by zero by returning None."""
    if b == 0:
        return None
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
    
    # Test multiplication - Corrected function called
    result = multiply(10, 5)
    print(f"10 * 5 = {result}")
    
    # Test division - Division by zero handled
    result = divide(10, 0)
    if result is None:
        print("Division by zero")
    else:
        print(f"10 / 0 = {result}")
    
    # Test power - Correct order of arguments
    result = power(2, 3)
    print(f"2 ^ 3 = {result}")
    
    # Define undefined variable
    count = 5
    print(f"Total calculations: {count}")
    
    print("=" * 40)
    print("Calculations complete!")
    """Multiply two numbers"""
    return a * b

def divide(a, b):
    """Divide a by b
    Handles division by zero by returning None."""
    if b == 0:
        return None
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
    
    # Test multiplication - Corrected function called
    result = multiply(10, 5)
    print(f"10 * 5 = {result}")
    
    # Test division - Division by zero handled
    result = divide(10, 0)
    if result is None:
        print("Division by zero")
    else:
        print(f"10 / 0 = {result}")
    
    # Test power - Correct order of arguments
    result = power(2, 3)
    print(f"2 ^ 3 = {result}")
    
    # Define undefined variable
    count = 5
    print(f"Total calculations: {count}")
    
    print("=" * 40)
    print("Calculations complete!")

if __name__ == "__main__":
    main()
