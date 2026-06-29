from random import randint

procurado = randint(1, 100) # número a ser procurado

inicio = 1
fim = 100

for i in range(1, 8): # temos 7 tentativas de acertar
    meio = (inicio + fim) // 2 # processo de busca binária
    print(f"\nSugestão: tente o número {meio}.")

    n = int(input(f"{i}a. tentativa de 7? "))

    if (n == procurado):
        print("\n\nParabéns, você acertou!!!")
        break

    if (i == 7):
        print("\n\nInfelizmente você errou as 7 tentativas.")
        break

    if (procurado < meio):
        fim = meio # procurado está na primeira parte: de início até meio
    else:
        inicio = meio # procurado está na segunda parte: de meio até fim