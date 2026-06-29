def digaOla():
    print("Olá!!!")

def digaOlaPara(nome):
    print("Olá Sr(a).", nome)

def boasVindas(nome, sexo):
    if (sexo == 'f') or (sexo == 'F'):
        print("Seja bem-vinda Sra.", nome)
    else:
        print("Seja bem-vindo Sr.", nome)  

# módulo principal (main)
digaOla()
digaOlaPara("Joaquim")
digaOlaPara("Vanessa")
boasVindas("Joaquim", "M")
boasVindas("Vanessa", "F")