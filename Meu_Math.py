from math import sqrt

def soma(a, b):
    return(a + b)

def sub(a, b):
    return(a - b)

def mult(a, b):
    return(a * b)

def divInt(a, b):
    return(a // b)

def resto(a, b):
    return(a % b)

def divReal(a, b):
    return(a / b)

def raizQuadrada(n):
    return(sqrt(n))

def divisores(n):
    div = []
    for i in range(1, n+1):
        if ((n % i) == 0):
            div.append(i)

    return(div)

def ehPrimo(n):
    return(len(divisores(n)) == 2)

def toString(a, b):
    result = f"{a} + {b} = {soma(a, b)}\n" + \
             f"{a} - {b} = {sub(a, b)}\n" + \
             f"{a} x {b} = {mult(a, b)}\n" + \
             f"{a} / {b} = {divInt(a, b)} divisão inteira\n" + \
             f"{a} % {b} = {resto(a, b)} resto da divisão inteira\n" + \
             f"{a} / {b} = {divReal(a, b):.2f} divisão real\n"
    return(result)