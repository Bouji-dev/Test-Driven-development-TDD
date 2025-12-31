

def multiply(a, b):
    if a is None or b is None:
        raise ValueError('Inputs cannot be None')
    return a * b

def is_even(n):
    if not isinstance(n, int):
        raise TypeError('Input must be an integer')
    return n % 2 == 0

