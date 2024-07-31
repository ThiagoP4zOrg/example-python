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
    assert Calculator.divide(1, 2) == 0.5
    assert Calculator.divide(1.0, 2.0) == 0.5
    assert Calculator.divide(0, 2.0) == 0.0
    assert Calculator.divide(-4, 2.0) == -2.0
    assert Calculator.divide(2.0, 0.0) == 'Cannot divide by 0'

def test_modulus():
    assert Calculator.modulus(10, 3) == 1
    assert Calculator.modulus(10, 0) == 'Cannot perform modulus operation with 0'
    assert Calculator.modulus(-4, 2) == 0
    assert Calculator.modulus(4, -2) == 0

def test_power():
    assert Calculator.power(2, 3) == 8.0
    assert Calculator.power(2.0, 3.0) == 8.0
    assert Calculator.power(2, 0) == 1.0
    assert Calculator.power(2.0, -2) == 0.25

def test_sqrt():
    assert Calculator.sqrt(16) == 4.0
    assert Calculator.sqrt(0) == 0.0
    assert Calculator.sqrt(1) == 1.0
    assert Calculator.sqrt(-16) == 'Cannot take square root of a negative number'

def test_log():
    assert Calculator.log(10) == 2.302585092994046
    assert Calculator.log(100, 10) == 2.0
    assert Calculator.log(-10) == 'Logarithm undefined for non-positive values'
    assert Calculator.log(0) == 'Logarithm undefined for non-positive values'

def test_factorial():
    assert Calculator.factorial(5) == 120
    assert Calculator.factorial(-5) == 'Factorial is not defined for negative numbers'
    assert Calculator.factorial(5.5) == 'Factorial is only defined for integers'

def test_sine():
    assert Calculator.sine(math.pi / 2) == 1.0
    assert Calculator.sine(0) == 0.0
    assert Calculator.sine(math.pi) == 1.2246467991473532e-16

def test_cosine():
    assert Calculator.cosine(math.pi) == -1.0
    assert Calculator.cosine(0) == 1.0
    assert Calculator.cosine(math.pi / 2) == 6.123233995736766e-17

def test_tangent():
    assert Calculator.tangent(math.pi / 4) == 1.0
    assert Calculator.tangent(0) == 0.0
    assert Calculator.tangent(math.pi) == -1.2246467991473532e-16
