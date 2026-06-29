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

def toString(a, b):
    result = f"{a} + {b} = {soma(a, b)}\n" + \
             f"{a} - {b} = {sub(a, b)}\n" + \
             f"{a} x {b} = {mult(a, b)}\n" + \
             f"{a} / {b} = {divInt(a, b)} divisão inteira\n" + \
             f"{a} % {b} = {resto(a, b)} resto da divisão inteira\n" + \
             f"{a} / {b} = {divReal(a, b):.2f} divisão real\n"
    return(result)
    
# módulo principal (main)
print(toString(7, 3))