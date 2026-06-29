from Calculadora_IMC import toString
from Geral import cls, parada

cls()

# 1a. etapa: abrir o arquivo texto no modo de leitura
arquivo = open("pacientes.txt", "r")

# 2a. etapa: ler "todas" as linhas do arquivo texto
linhas = arquivo.readlines()
for linha in linhas:
    cls()
    
    partes = linha.split("; ")
    
    paciente = partes[0]
    pc = float(partes[1])
    alt = float(partes[2])
    
    print(toString(paciente, pc, alt))

    parada()

# 3a. etapa: fechar o arquivo texto (SEMPRE)
arquivo.close()
