casasdelujo = str(input(": "))
apartamentoslujo = str(input(": "))
listadodeventas = str(input(": "))

contadorcasasdelujo = 0
contadorapartamentoslujo = 0
resultadoanalisis = ""

for elemento in listadodeventas:
    haycasas = elemento in casasdelujo
    hayaptos = elemento in apartamentoslujo

    if haycasas == True and hayaptos == False:
        contadorcasasdelujo = contadorcasasdelujo + 1
    elif haycasas == False and hayaptos == True:
        contadorapartamentoslujo = contadorapartamentoslujo + 1
    elif haycasas == True and hayaptos == True:
        contadorcasasdelujo = contadorcasasdelujo + 1
        contadorapartamentoslujo = contadorapartamentoslujo + 1

    if contadorcasasdelujo > contadorapartamentoslujo:
        resultadoanalisis = resultadoanalisis + "C"
    elif contadorcasasdelujo < contadorapartamentoslujo:
        resultadoanalisis = resultadoanalisis + "A"
    elif contadorcasasdelujo == contadorapartamentoslujo:
        resultadoanalisis = resultadoanalisis + "N"

print(resultadoanalisis)