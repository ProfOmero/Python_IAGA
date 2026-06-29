def mostrar(n):
    print("{", end=" ")
    for i in range(1, n+1):
        print(i, end=" ")
    print("} ", end="")

def somar(n):
    sm = 0
    for i in range(1, n+1):
        sm = sm + i
    return(sm)

def resultados(n):        
    mostrar(n)
    print("soma =", somar(n))

# módulo principal (main)
resultados(9)
resultados(7)