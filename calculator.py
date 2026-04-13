import math


def square_root(a):
    if a < 0:
        raise ValueError("Cant calculate square root of a negative number")
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
    try:
        return a / b
    except ZeroDivisionError:
        raise ZeroDivisionError("Cant divide by zero")

def logarithm(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("Logarithm args must be positive")
    return math.log(a, b)

def exp(a, b):
    return a ** b