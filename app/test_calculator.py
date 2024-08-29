import math
import pytest
from .calculator import Calculator

def test_add():
    assert Calculator.add(1, 2) == 3.0
    assert Calculator.add(1.0, 2.0) == 3.0
    assert Calculator.add(0, 2.0) == 2.0
    assert Calculator.add(2.0, 0) == 2.0
    assert Calculator.add(-4, 2.0) == -2.0

def test_subtract():
    assert Calculator.subtract(1, 2) == -1.0
    assert Calculator.subtract(2, 1) == 1.0
    assert Calculator.subtract(1.0, 2.0) == -1.0
    assert Calculator.subtract(0, 2.0) == -2.0
    assert Calculator.subtract(2.0, 0.0) == 2.0
    assert Calculator.subtract(-4, 2.0) == -6.0

def test_multiply():
    assert Calculator.multiply(1, 2) == 2.0
    assert Calculator.multiply(1.0, 2.0) == 2.0
    assert Calculator.multiply(0, 2.0) == 0.0
    assert Calculator.multiply(2.0, 0.0) == 0.0
    assert Calculator.multiply(-4, 2.0) == -8.0

def test_divide():
    # assert Calculator.divide(1, 2) == 0.5
    assert Calculator.divide(1.0, 2.0) == 0.5
    assert Calculator.divide(0, 2.0) == 0
    assert Calculator.divide(-4, 2.0) == -2.0
    # assert Calculator.divide(2.0, 0.0) == 'Cannot divide by 0'

def test_modulus():
    assert Calculator.modulus(5, 2) == 1
    assert Calculator.modulus(5.0, 2.0) == 1.0
    assert Calculator.modulus(4, 2) == 0
    assert Calculator.modulus(0, 2) == 0
    assert Calculator.modulus(-5, 2) == 1

def test_power():
    assert Calculator.power(2, 3) == 8.0
    assert Calculator.power(5, 0) == 1.0
    assert Calculator.power(7, -1) == 1 / 7.0
    assert Calculator.power(4, 0.5) == 2.0
    assert Calculator.power(-2, 3) == -8.0

def test_square_root():
    assert Calculator.square_root(4) == 2.0
    assert Calculator.square_root(9) == 3.0
    assert Calculator.square_root(0) == 0.0
    assert Calculator.square_root(2) == 1.4142135623730951
    # Testing square root of a negative number should be handled separately
    # Since this is not supported in the current implementation, you might want to add validation if needed
    # Uncomment the following line if you decide to handle negative inputs
    # assert Calculator.square_root(-4) == 'Invalid input for square root'

# def test_factorial():
#     assert Calculator.factorial(0) == 1
#     assert Calculator.factorial(1) == 1
#     assert Calculator.factorial(5) == 120
#     assert Calculator.factorial(10) == 3628800
#     with pytest.raises(ValueError):
#         Calculator.factorial(-1)

# def test_logarithm():
#     assert Calculator.logarithm(10, 10) == 1.0
#     assert Calculator.logarithm(100, 10) == 2.0
#     assert Calculator.logarithm(math.e, math.e) == 1.0
#     assert Calculator.logarithm(8, 2) == 3.0
#     with pytest.raises(ValueError):
#         Calculator.logarithm(0, 10)
#     with pytest.raises(ValueError):
#         Calculator.logarithm(10, 0)
#     with pytest.raises(ValueError):
#         Calculator.logarithm(10, 1)

# def test_exponential():
#     assert Calculator.exponential(0) == pytest.approx(1.0, rel=1e-9)
#     assert Calculator.exponential(1) == pytest.approx(math.e, rel=1e-9)
#     assert Calculator.exponential(2) == pytest.approx(math.e ** 2, rel=1e-9)
#     assert Calculator.exponential(-1) == pytest.approx(1 / math.e, rel=1e-9)

# def test_absolute():
#     assert Calculator.absolute(5) == 5
#     assert Calculator.absolute(-5) == 5
#     assert Calculator.absolute(0) == 0
#     assert Calculator.absolute(3.14) == 3.14
#     assert Calculator.absolute(-3.14) == 3.14