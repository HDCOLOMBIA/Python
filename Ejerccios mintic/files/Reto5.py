def cancion_sin_repeticiones(listacanciones):
    listasinrep = []
    for item in listacanciones:
        if item not in listasinrep:
            listasinrep.append(item)
    return listasinrep


def posiciones_con_cancion(listadeposiciones, listacanciones2, numeroentero):

    resultadoposicion = []
    for x in listadeposiciones:
        if numeroentero == listacanciones2[x]:
            resultadoposicion.append(x)
    return resultadoposicion


def solo_categoria_x(categoria_x, categoria_y):

    soloen_categoria_x = []
    for element in categoria_x:
        if element not in categoria_y:
            soloen_categoria_x.append(element)
    return soloen_categoria_x


def cantidad_cambios(usuario1, usuario2):
    contadorusuario1 = 0
    contadorusuario2 = 0
    cambiosposibles = 0

    for element in usuario1:
        if element not in usuario2:
            contadorusuario1 += 1

    for element2 in usuario2:
        if element2 not in usuario1:
            contadorusuario2 += 1

    if contadorusuario1 < contadorusuario2:
        cambiosposibles = contadorusuario1
    else:
        cambiosposibles = contadorusuario2

    return cambiosposibles
