import math

class Calculator:

    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract(x, y):
        return x - y

    @staticmethod
    def multiply(x, y):
        return x * y

    @staticmethod
    def divide(x, y):
        try:
            return x / y
        except ZeroDivisionError:
            return 'Cannot divide by 0'

    @staticmethod
    def modulus(x, y):
        try:
            return x % y
        except ZeroDivisionError:
            return 'Cannot perform modulus operation with 0'

    @staticmethod
    def power(x, y):
        return x ** y

    @staticmethod
    def sqrt(x):
        if x < 0:
            return 'Cannot take square root of a negative number'
        return math.sqrt(x)

    @staticmethod
    def log(x, base=math.e):
        if x <= 0:
            return 'Logarithm undefined for non-positive values'
        return math.log(x, base)

    @staticmethod
    def factorial(x):
        if x < 0:
            return 'Factorial is not defined for negative numbers'
        if not isinstance(x, int):
            return 'Factorial is only defined for integers'
        return math.factorial(x)

    @staticmethod
    def sine(x):
        return math.sin(x)

    @staticmethod
    def cosine(x):
        return math.cos(x)

    @staticmethod
    def tangent(x):
        return math.tan(x)

# Example usage:
calc = Calculator()

print(calc.add(10, 5))           # 15
print(calc.subtract(10, 5))      # 5
print(calc.multiply(10, 5))      # 50
print(calc.divide(10, 5))        # 2.0
print(calc.divide(10, 0))        # 'Cannot divide by 0'
print(calc.modulus(10, 3))       # 1
print(calc.modulus(10, 0))       # 'Cannot perform modulus operation with 0'
print(calc.power(2, 3))          # 8
print(calc.sqrt(16))             # 4.0
print(calc.sqrt(-16))            # 'Cannot take square root of a negative number'
print(calc.log(10))              # 2.302585092994046 (natural log)
print(calc.log(100, 10))         # 2.0 (log base 10)
print(calc.factorial(5))         # 120
print(calc.factorial(-5))        # 'Factorial is not defined for negative numbers'
print(calc.sine(math.pi / 2))    # 1.0
print(calc.cosine(math.pi))      # -1.0
print(calc.tangent(math.pi / 4)) # 1.0
