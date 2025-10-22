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

def multiply(a, b)
    """Multiply two numbers"""
    return a * b

def divide(a, b):
    """Divide a by b"""
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
    
    # Test multiplication - BUG: Wrong function called
    result = add(10, 5)
    print(f"10 * 5 = {result}")
    
    # Test division - BUG: Division by zero not handled
    result = divide(10, 0)
    print(f"10 / 0 = {result}")
    
    # Test power - BUG: Wrong order of arguments
    result = power(3, 2)
    print(f"2 ^ 3 = {result}")
    
    # BUG: Undefined variable
    print(f"Total calculations: {count}")
    
    print("=" * 40)
    print("Calculations complete!"

if __name__ == "__main__":
    main()
