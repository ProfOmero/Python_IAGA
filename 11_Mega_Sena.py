from random import randint
from Vetor import saida

while True:
    n = int(input("Quantidade de cartões (no máximo 10, -1 para encerrar)? "))
    if (n == -1):
        break

    if ((n < 1) or (n > 10)):
       print(f"Erro: {n}, quantidade de cartões inválida!!!")
       print()
       continue

    print()
    no_Jogo = []
    for i in range(n):
        jogo = []
        j = 1
        while (j <= 6): # faz um jogo de 6 números
            nro = randint(1, 60)
            if (nro not in no_Jogo):
                jogo.append(nro)
                no_Jogo.append(nro)
                j = j + 1

        print(saida(f"{i+1}o. jogo", sorted(jogo)))

    print()