#IntegerPlus Source Code

def add(firstint,secondint):
    return firstint+secondint

def subtract(firstint,secondint):
    return firstint - secondint

def divide(firstint,secondint):
    return firstint/secondint

def square(int):
    return int*int

def cube(int):
    return int*int*int

def half(int):
    return int/2

def quarter(int):
    return int/4

def third(int):
    return int/3

def double(int):
    return int*2

def triple(int):
    return int*3

def quadrouple(int):
    return int*4

def clamp(int,min,max):
    if int > max:
        int = max
    elif int < min:
        int = min
    return int

def max(int,max):
    if int > max:
        int = max
    return int

def min(int,min):
    if int < min:
        int = min
    return int

def pow(intone,inttwo):
    return intone^inttwo
