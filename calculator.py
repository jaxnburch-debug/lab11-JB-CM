# https://github.com/jaxnburch-debug/lab11-JB-CM
# Partner 1: Jackson Burch
# Partner 2: Christian Mason

def add(a, b):
    return a + b

import math

def square_root(a):
    if a < 0:
        raise ValueError("Cant calculate sqrt of negative")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a

def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError
    return math.log(b, a)

def exp(a, b):
    return a ** b