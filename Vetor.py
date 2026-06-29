def entrada(id, tam):
    x = []
    for i in range(tam):
        x.append(int(input(f"{i+1}o. valor: {id}[{i}] = ")))
    print()

    return(x)

def saida(id, x):
    tam = len(x)

    result = f"{id} = ["
    for i in range(tam):
        result = result + f"{x[i]}"
        if (i != (tam-1)):
            result = result + ", "
    result = result + "]"

    return(result)

def somar(x):
    return(sum(x))

def media(x):
    return(sum(x) / len(x))

def toString(id, x):
    result = saida(id, x) + \
             f"\n\nSoma dos Valores = {somar(x)}\n" + \
             f"Valor Médio      = {media(x)}\n"
    return(result)