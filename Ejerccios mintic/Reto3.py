entrada = input()
entradaSinEspacios = entrada.split(" ")

salidaLetras = ""
salidaNumeros = ""
contadorTemporal = 0
itemTemporal = ""

for index, item in enumerate(entradaSinEspacios):
    if item == itemTemporal:
        contadorTemporal = contadorTemporal + 1
    else:
        contadorTemporal = 1
        salidaLetras = salidaLetras + item + ' '
    itemTemporal = item

    try:
        existeItemFuturo = item == entradaSinEspacios[index+1]
    except:
        existeItemFuturo = False

    if existeItemFuturo:
        bool
    else:
        salidaNumeros = salidaNumeros + str(contadorTemporal) + " "

salidaLetras = salidaLetras.rstrip(' ')
salidaNumeros = salidaNumeros.rstrip(' ')

print(salidaLetras)
print(salidaNumeros)
