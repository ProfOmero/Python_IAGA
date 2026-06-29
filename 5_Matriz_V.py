def matriz(nl, nc):
    for i in range(nl):
        for j in range(i):
            print("**", end=" ")

        for j in range(i, nc):
            print(f"{i}{j}", end=" ")

        print()

# módulo principal (main)
nl = int(input("Quantas linhas na matriz? "))
nc = int(input("Quantas colunas na matriz? "))

print()
matriz(nl, nc)