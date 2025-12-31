

def multiply(a, b):
    if a is None or b is None:
        raise ValueError('Inputs cannot be None')
    return a * b

def is_even(n):
    if not isinstance(n, int):
        raise TypeError('Input must be an integer')
    return n % 2 == 0

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError('Division by zero is not allowed')
    if not isinstance(a, (int | float)) or not isinstance(b, (int | float)):
        raise TypeError('Inputs must be an integer or float')
    return a / b