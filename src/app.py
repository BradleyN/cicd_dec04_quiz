import numpy as np
import cmath

def add(a, b):
    if not isinstance(a, (int,float,complex)) or not isinstance(a, (int,float,complex)):
        return None
    return a+b

def sub (a, b):
    if not isinstance(a, (int,float,complex)) or not isinstance(a, (int,float,complex)):
        return None
    
    return a-b

def mul (a, b):
    if not isinstance(a, (int,float,complex)) or not isinstance(a, (int,float,complex)):
        return None
    
    result = a*b

    return complex_round(result)

def div(a,b):
    if not isinstance(a, (int,float,complex)) or not isinstance(a, (int,float,complex)):
        return None
    
    if isinstance(a,int):
        a = float(a)
    if isinstance(b,int):
        b = float(b)

    if b == 0:
        return None
    
    result = a/b
    return complex_round(result)


def log(x):
    if not isinstance(x, (int,float,complex)):
        return None
    
    if isinstance(x, complex):
        if x == 0+0j:
            return None
    elif x <= 0:
        return None
    
    return cmath.log(x)

def power(x,n):
    if not isinstance(x, (int,float,complex)) or not isinstance(n, (int,float,complex)):
        return None
    
    if isinstance(n, complex):
        if x == 0:
            return None
    elif x == 0 and n < 0:
        return None
    
    return np.pow(x,n)

def sin(theta):
    if not isinstance(theta, (int,float,complex)):
        return None

    return complex_round(np.sin(theta))

def cos(theta):
    if not isinstance(theta, (int,float,complex)):    
        return None

    return complex_round(np.cos(theta))

def sqrt(x):
    if not isinstance(x, (int,float,complex)):
        return None
    
    if isinstance(x, (int, float)):
        if x < 0:
            real = 0
            imag = np.sqrt(abs(x))
            return complex(real,imag)
    return np.sqrt(x)

def complex_round(value):
    if isinstance(value, complex):
        real = round(value.real, 10)
        imag = round(value.imag, 10)
        value = complex(real, imag)
    else:
        value = round(value,10)

    return value