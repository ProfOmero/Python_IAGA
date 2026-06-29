def matriz_I(n):
    i = 0 # variável de controle da linha
    while (i < n):
        j = 0 # variável de controle da coluna
        while (j < n):
            print(f"{i}{j}", end=" ")
            j = j + 1 # coluna
        print()
        i = i + 1 # linha

def matriz_II(n):
    for i in range(n):
        for j in range(n):
            print(f"{i}{j}", end=" ")
        print()

# módulo principal (main)
n = int(input("Tamanho da matriz? "))

print()
matriz_I(n)
print()
matriz_II(n)