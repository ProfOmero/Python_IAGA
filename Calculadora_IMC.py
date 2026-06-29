def calcular_IMC(pc, alt):
    return(pc / (alt ** 2))

def interpretar_IMC(vlr_IMC):
    if (vlr_IMC < 18.5):
        interpretacao = "Magreza"
    elif (vlr_IMC < 25.0):
        interpretacao = "Normal"
    elif (vlr_IMC < 30.0):
        interpretacao = "Sobrepeso"
    elif (vlr_IMC < 40.0):
        interpretacao = "Obesidade"
    else:
        interpretacao = "Obesidade Grave"

    return(interpretacao)

def toString(paciente, pc, alt):
    vlr_IMC = calcular_IMC(pc, alt)

    result = f"Nome do Paciente: {paciente}\n" + \
             f"Peso Corporal...: {pc:.3f} kgs\n" + \
             f"Altura..........: {alt:.2f} metros\n" + \
             f"Valor do IMC....: {vlr_IMC:.2f} <<< {interpretar_IMC(vlr_IMC)} >>>"
    
    return(result)