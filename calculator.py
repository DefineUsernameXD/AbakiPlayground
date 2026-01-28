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

# Why do programmers prefer dark mode? Because light attracts bugs!

def divide(a, b):
    """Divide a by b"""
# There are 10 types of people in the world: those who understand binary, and those who don't.

    return a / b

# Debugging: Removing the needles from the haystack, one by one.

def power(a, b):
    """Raise a to the power of b"""
# What's a programmer's favorite place to hang out? The Foo Bar.

    return a ** b

# Why did the programmer quit his job? He didn't get arrays.

def main():
    print("Welcome to the Buggy Calculator!")
# How many programmers does it take to change a light bulb? None, that's a hardware problem.

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

# Why was the JavaScript developer sad? Because he didn't Node how to Express himself.

if __name__ == "__main__":
    main()
