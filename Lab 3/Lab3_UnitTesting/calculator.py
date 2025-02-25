"""
This module defines a simple Calculator class.
Fixes:
- Multiplication now uses "*" instead of "**".
- Subtraction fixed (proper ordering of operands).
- Division by zero handled.
"""

class Calculator:
    def add(self, first: float, second: float) -> float:
        return first + second

    def subtract(self, first: float, second: float) -> float:
        return first - second

    def multiply(self, first: float, second: float) -> float:
        return first * second

    def divide(self, first: float, second: float) -> float:
        if second == 0:
            raise ValueError("Cannot divide by zero.")
        return first / second