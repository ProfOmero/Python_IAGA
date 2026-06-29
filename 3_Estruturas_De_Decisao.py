def sinal_I(n):
    if (n < 0):
        return("<<< negativo >>>")
    
    if (n == 0):
        return("<<< neutro >>>")
    
    if (n > 0):
        return("<<< positivo >>>")
    
def sinal_II(n):
    if (n < 0):
        return("<<< negativo >>>")
    else:
        if (n == 0):
            return("<<< neutro >>>")
        else:
            return("<<< positivo >>>")
    
def sinal_III(n):
    if (n < 0):
        return("<<< negativo >>>")
    elif (n == 0):
        return("<<< neutro >>>")
    else:
        return("<<< positivo >>>")
    
# módulo principal (main)
n = int(input("Quantos valores serão informados? "))

for i in range(1, n+1):
    print()

    valor = int(input(f"{i}o. valor: "))

    print(sinal_I(valor))
    print(sinal_II(valor))
    print(sinal_III(valor))