def linha(tipo="*", tam=20):
    result = ""
    for i in range(tam):
        result = result + tipo

    return(result)

# módulo principal (main)
# por onde começa a execução desta estrutura modular
print(linha("*", 20))
print(linha())
print(linha(tipo="X"))
print(linha(tipo="@", tam=50))
print(linha("@", 50))
print(linha(tam=50))
print(linha("<<< ABC >>>", 5))