import Geral

Geral.cls()
# 1a. etapa: abrir o arquivo texto no modo de abertura adequado
arquivo = open("pacientes.txt", "a")

n = int(input("Informe a quantidade de pacientes que serão cadastrados? "))
for i in range(n):
    Geral.cls()
    paciente = input("Nome do Paciente......: ")
    pc = float(input("Peso Corporal (em kgs): "))
    alt = float(input("Altura (em metros)....: "))

    if (Geral.confirmou("\nCadastrar Paciente (S/*)? ")):
        # 2a. etapa: gravar no arquivo texto
        arquivo.write(f"{paciente}; {pc}; {alt}\n")
        
        print("<<< Paciente cadastrado com sucesso!!! >>>")
        Geral.delay(1)

# 3a. etapa: fechar o arquivo texto
arquivo.close()