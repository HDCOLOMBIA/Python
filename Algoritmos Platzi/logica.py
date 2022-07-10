'''
while condición:
    bloque código
'''
'''
for i in secuencia:
    bloque código
'''
#Cree un programa con base anterior con sentencias If, Elif y Else, para que pueda comprar el nombre del persona y pueda imprimir sus caracteristicas

personaje = str.upper(input(f"Escriba aquí el personaje Akatsuki: "))
habilidad = str.upper(input(f"Escriba su habilidad: "))

if personaje == "ITACHI" and habilidad == "AMATERASU":
    print(f'\nSu personaje es: ', personaje, '\nSu habilidad es:', habilidad,)

elif personaje == "TOBI" and habilidad == "KAMUI":
    print(f'\nSu personaje es: ', personaje, '\nSu habilidad es:', habilidad,)

elif personaje == "SASORI" and habilidad == "MARIONETAS":
    print(f'\nSu personaje es: ', personaje, '\nSu habilidad es: ', habilidad,)

elif personaje == "OROCHIMARU" and habilidad == "CULEBRON":
    print(f'\nSu personaje es: ', personaje, '\nSu habilidad es: ', habilidad,)

elif personaje == "PAIN" and habilidad == "RINNEGAN":
    print(f'\nSu personaje es: ', personaje, '\nSu habilidad es: ', habilidad,)

elif personaje == "KONAN" and habilidad == "PAPEL":
    print(f'\nSu personaje es: ', personaje, '\nSu habilidad es: ', habilidad,)

elif personaje == "KAKUZU" and habilidad == "MULTIELEMENTAL":
    print(f'\nSu personaje es: ', personaje,'\nSu habilidad es: .', habilidad,)

elif personaje == "HIDAN" and habilidad == "RITUAL DE HASHIN":
    print(f'\nSu personaje es: ', personaje, '\nSu habilidad es: ', habilidad,)

elif personaje == "DEIDARA" and habilidad == "TITERES":
    print(f'\nSu personaje es: ', personaje, '\nSu habilidad es: ', habilidad,)

else:
    print(f'\nEl personaje', personaje, 'que indico o la habilidad',habilidad,'no son de Akatsuki, imbecil')


