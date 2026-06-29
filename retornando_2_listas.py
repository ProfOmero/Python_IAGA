def separar(a):
    pares = []
    impares = []

    for i in range(len(a)):
        if ((a[i] % 2) == 0):
            pares.append(a[i])
        else:
            impares.append(a[i])

    return(pares, impares)

# módulo principal (main)
x = [7, 1, 4, 3, 7, 8]

pares, impares = separar(x)

print(x)
print(pares)
print(impares)