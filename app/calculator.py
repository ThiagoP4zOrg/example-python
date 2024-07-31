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
