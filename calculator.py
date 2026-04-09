import math
521309984bf35c270bea4f4f9864cf5e778b8518

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