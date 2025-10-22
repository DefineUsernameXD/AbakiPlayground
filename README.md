# AbakiPlayground

A simple Python playground with intentional coding errors for practice debugging and fixing bugs.

## Overview

This repository contains a simple calculator program (`calculator.py`) with **6 intentional errors** that need to be fixed. This is a great exercise for learning debugging skills!

## Error Types

The code contains:
- **2 Syntax Errors** - Code won't even run until these are fixed
- **2 Logic Errors** - Code runs but produces wrong results
- **2 Runtime Errors** - Code runs but crashes during execution

## Getting Started

### Prerequisites
- Python 3.6 or higher

### Running the Buggy Code

```bash
python calculator.py
```

You'll immediately encounter errors! Your job is to find and fix all 6 bugs.

### Challenge

Try to fix all the errors without looking at the solutions first! Here's a suggested approach:

1. **Fix syntax errors first** - The code won't run until these are fixed
2. **Handle runtime errors** - Prevent crashes during execution
3. **Debug logic errors** - Make sure the calculations are correct

### Hints

- Read error messages carefully - they often tell you exactly what's wrong
- Check function definitions for proper syntax
- Verify that you're calling the correct functions
- Make sure all variables are defined before use
- Watch out for mathematical operations that could cause errors
- Check that print statements are properly formatted

### Solutions

If you get stuck, check the `SOLUTIONS.md` file for detailed explanations of each error and how to fix it.

## Expected Output (After All Fixes)

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

## Learning Objectives

- Understand different types of errors (syntax, runtime, logic)
- Practice reading and interpreting error messages
- Develop debugging skills
- Learn to test code systematically

Happy debugging! 🐛🔧