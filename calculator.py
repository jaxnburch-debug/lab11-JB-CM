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

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        raise ZeroDivisionError("Cant divide by zero")

def logarithm(a, b):
    return math.log(a, b)

def exponent(a, b):
    return a ** b