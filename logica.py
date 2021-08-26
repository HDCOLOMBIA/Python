'''
while condición:
    bloque código
'''
'''
for i in secuencia:
    bloque código
'''
#Cree un programa con base anterior con sentencias If, Elif y Else, para que pueda comprar el nombre del persona y pueda imprimir sus caracteristicas


personaje = str.upper(input("ingresar su akatsuki: "))
if personaje == "ITACHI":
    print(f'\nSu personaje es: ',personaje, '\nSu habilidad es: Amaterasu.')
elif personaje == "TOBI":
    print(f'\nSu personaje es: ',personaje, '\nSu habilidad es: Kamui.')
elif personaje == "SASORI":
    print(f'\nSu personaje es: ',personaje, '\nSu habilidad es: Marionetas.')
elif personaje == "OROCHIMARU":
    print(f'\nSu personaje es: ',personaje, '\nSu habilidad es: el culebron.')
elif personaje == "PAIN":
    print(f'\nSu personaje es: ',personaje, '\nSu habilidad es: Rinnegan.')
elif personaje == "KONAN":
    print(f'\nSu personaje es: ',personaje, '\nSu habilidad es: Papeles.')
elif personaje == "KAKUZU":
    print(f'\nSu personaje es: ',personaje, '\nSu habilidad es: Multielemental.')
elif personaje == "HIDAN":
    print(f'\nSu personaje es: ',personaje, '\nSu habilidad es: Ritual del Hashin.')
elif personaje == "DEIDARA":
    print(f'\nSu personaje es: ',personaje, '\nSu habilidad es: Bobas Explosivas.')
else:
    print(f'\nEl personaje' ,personaje, 'que indico no esta en Akatsuki, imbecil')
