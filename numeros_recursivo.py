def mostrar(i, n):
    if (i <= n):
        if (i == 1):
            print("{", end=" ")
        print(i, end=" ")
        i = i + 1
        mostrar(i, n) # chamada recursiva
    else:
        print("} ", end="")

def somar(i, n):
    if (i <= n):
        novoI = i + 1
        return(i + somar(novoI, n)) # chamada recursiva
    else:
        return(0)

def resultados(n):        
    mostrar(1, n)
    print("soma =", somar(1, n))

# módulo principal (main)
resultados(9)
resultados(7)