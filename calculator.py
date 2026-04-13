<<<<<<< HEAD
# https://github.com/jaxnburch-debug/lab11-JB-CM
# Partner 1: Jackson Burch
# Partner 2: Christian Mason
=======
import math

def add(a, b):
    return a + b
>>>>>>> 46e4a66031f6c499f1601c607995ec4988b769f4

import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a

def log(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError
    return math.log(b, a)

def exp(a, b):
    return a ** b