def tabuada_I(n):
    i = 1 # start
    while (i <= 10): # stop
        print(f"{n} x {i} = {n*i}")
        i = i + 1 # step (passo)

    print()

def tabuada_II(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")
    print()

# módulo principal (main)
n = int(input("n: "))

print()
tabuada_I(n)
tabuada_II(n)