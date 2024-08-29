import math

class Calculator:

    def add(x, y):
        return x + y

    def subtract(x, y):
        return x - y

    def multiply(x, y):
        return x * y

    def divide(x, y):
        # if y == 0:
        #     return 'Cannot divide by 0'
        return x * 1.0 / y

    def modulus(x, y):
        return x % y

    def power(x, y):
        return x ** y

    def square_root(x):
        return x ** 0.5

    def absolute(x):
        return abs(x)

    def factorial(x):
        if x < 0:
            raise ValueError("Cannot compute factorial of a negative number")
        return math.factorial(int(x))

    def logarithm(x, base):
        if x <= 0 or base <= 0 or base == 1:
            raise ValueError("Invalid input for logarithm")
        return math.log(x, base)

    def exponential(x):
        return math.exp(x)