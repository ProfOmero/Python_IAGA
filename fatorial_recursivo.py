def fatorial(n):
    if (n < 0):
        return(0)
    else:
        f = 1
        for i in range(1, n+1):
            f = f * i
        return(f)
    
def fatorial_recursivo(n):
    if (n < 0):
        return(0)
    elif (n == 0):
        return(1)
    else:
        return(n * fatorial_recursivo(n-1)) # chamada recursiva

# módulo principal (main)
n = int(input("n: "))

print()
print(f"{n}! = {fatorial(n)}")
print(f"{n}! = {fatorial_recursivo(n)}")