from math import sqrt, pow
from random import randint

n = int(input("n: "))

print()
print(f"Raiz quadrada = {sqrt(n):.4f}")
print(f"Cubo de {n} = {pow(n, 3):.0f}")

print()
a = []
for i in range(10):
    a.append(randint(1, 100)) # randint = sorteia uma aleatório inteiro

a.sort()
print(a)
