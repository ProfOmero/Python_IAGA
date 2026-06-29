from math import sqrt

def dobro(n):
    return(2 * n)

def triplo(n):
    return(3 * n)

def quadrado(n):
    return(n ** 2)

def cubo(n):
    return(n ** 3)

def raizQuadrada(n):
    return(sqrt(n))

def toString(n):
    result = f"Sendo n = {n}, tem-se:\n" + \
             f"Dobro         = {dobro(n)}\n" + \
             f"Triplo        = {triplo(n)}\n" + \
             f"Quadrado      = {quadrado(n)}\n" + \
             f"Cubo          = {cubo(n)}\n" + \
             f"Raiz Quadrada = {raizQuadrada(n):.4f}"
    return(result)

# módulo principal (main)
n = int(input("n: "))

print()
print(toString(n))