# Calculator Bug Fixes

This document lists all the intentional errors in `calculator.py` and how to fix them.

## Errors to Fix:

### 1. Syntax Error - Missing colon
**Line 14:** `def multiply(a, b)`
- **Error:** Missing colon at the end of function definition
- **Fix:** Add `:` at the end: `def multiply(a, b):`

### 2. Logic Error - Wrong function called
**Line 36:** `result = add(10, 5)`
- **Error:** Called `add()` instead of `multiply()`
- **Fix:** Change to: `result = multiply(10, 5)`
- **Expected output:** Should print "10 * 5 = 50" instead of "10 * 5 = 15"

### 3. Runtime Error - Division by zero
**Line 40:** `result = divide(10, 0)`
- **Error:** Division by zero will cause a ZeroDivisionError
- **Fix:** Add error handling or change to a valid divisor like `divide(10, 2)`
- **Better fix:** Add try-except block or check in the divide function

### 4. Logic Error - Wrong argument order
**Line 45:** `result = power(3, 2)`
- **Error:** Arguments are in wrong order (prints "2 ^ 3 = 8" but calculates 3^2 = 9)
- **Fix:** Change to: `result = power(2, 3)` to match the print statement

### 5. Runtime Error - Undefined variable
**Line 48:** `print(f"Total calculations: {count}")`
- **Error:** Variable `count` is never defined
- **Fix:** Define count variable or remove this line, or set `count = 5` before using it

### 6. Syntax Error - Missing closing quote
**Line 51:** `print("Calculations complete!")`
- **Error:** Missing closing quote
- **Fix:** Add closing quote: `print("Calculations complete!")`

## Summary
Total errors: 6
- Syntax errors: 2
- Logic errors: 2
- Runtime errors: 2

## Running the Code
To see the errors:
```bash
python calculator.py
```

After fixing all errors, the output should be:
```
Welcome to the Buggy Calculator!
========================================
10 + 5 = 15
10 - 5 = 5
10 * 5 = 50
10 / 2 = 5.0
2 ^ 3 = 8
Total calculations: 5
========================================
Calculations complete!
```
