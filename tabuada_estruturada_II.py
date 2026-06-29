def tabuada(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")

    print()

# módulo principal (main)
n = int(input("n: "))

print()

tabuada(n)