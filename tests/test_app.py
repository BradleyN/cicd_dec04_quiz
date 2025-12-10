import sys
import numpy as np
import math
from pathlib import Path

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "src"))


from app import add,sub,mul,div,sqrt,sin,cos,power,log

def test_add():
    assert add(5, 6) == 11
    assert add("a","b") is None
    assert add(1.0, 2.0) == 3.0
    assert add(1+2j, 2+3j) == 3+5j

def test_sub():
    assert sub(5, 6) == -1
    assert sub("a","b") is None
    assert sub(3.2, 2.1) == 1.1
    assert sub(1+2j, 2+3j) == -1-1j

def test_mul():
    assert mul("hi","there") is None
    assert mul(3,6) == 18
    assert mul(2,0.5) == 1
    assert mul(0.05, 0.05) == 0.0025
    assert mul(1+1j,1-1j) == 2
    #avoid float rounding errors by having the implementation of mult truncate the results.
    assert mul(0.000001,0.000001) == 0

def test_div():
    assert div(1,2) == 0.5
    assert div(1.0,3.0) == 0.3333333333
    assert div(1.0,1j) == -1j
    assert div("a","b") is None
    assert div(0.00000002,0.00000001) == 2
    assert div(5,0) is None

def test_log():
    assert log(-1) is None
    assert log(np.e) == 1
    assert log("hello") is None
    assert log(0+0j) is None
    assert log(0) is None

def test_power():
    assert power("1","2") is None
    assert power(1,2) == 1
    assert power(3,3) == 27
    assert power(4,0.5) == 2.0
    assert power(0+1j,2) == -1
    assert power(0,1+1j) is None
    assert power(0,-1) is None
    assert power(0,3) == 0

def test_sin():
    assert sin("hi") is None

    result = sin(np.pi)
    assert result is not None
    assert result == 0

    assert sin(0) == 0
    assert sin(1j) == complex(0,round(np.sinh(1),10))

    result = sin(3.141592)
    assert isinstance(result, float)
    assert result < 0.000001 


def test_cos():
    assert cos("hi") is None

    result = cos(np.pi / 2.0)
    assert isinstance(result, float)
    assert result == 0

    assert cos(0) == 1
    assert cos(1j) == complex(round(np.cosh(1),10),0)

    result = cos(3.141592)
    assert isinstance(result, float)
    assert result < 0.000001 

def test_sqrt():
    assert sqrt("hello there") is None
    assert sqrt(-1) == 0+1j

    temp = sqrt(2.3)
    assert isinstance(temp,float)
    assert sqrt(-2.3) == complex(0,temp)

    assert sqrt(4) == 2