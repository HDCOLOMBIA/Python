""" Ejercicio 2
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al
usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario
coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
"""

# password = 'contraseña'
# user_password = str(input('Ingrese su clave: \n')).lower()

# if user_password == password:
#     print('Su contraseña es correcta')
# else:
#     print('Su contraseña es incorrecta')

""" Ejercicio 8
En una determinada empresa, sus empleados son evaluados al final de cada año.
Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir
aumentando, traduciéndose en mejores beneficios. Los puntos que pueden conseguir
los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre
las cifras mencionadas. A continuación se muestra una tabla con los niveles
correspondientes a cada puntuación. La cantidad de dinero conseguida en cada
nivel es de 2.400€ multiplicada por la puntuación del nivel.
"""

nivel = float(input('Introduzca su puntaje desde 0.0, 0.4, 0.6 o más: \n'))

if nivel == 0.0:
    print(f'El puntaje actual {nivel}, lo deja en el nivel Inaceptable. Por lo tanto recibirá {nivel*2400}€')
elif nivel == 0.4:
    print(f'El puntaje actual {nivel}, lo deja en el nivel Aceptable. Por lo tanto recibirá {nivel*2400}€')
elif nivel >= 0.6:
    print(f'El puntaje actual {nivel}, lo deja en el nivel Meritorio. Por lo tanto recibirá {nivel*2400}€')
else:
    print(f'El valor del puntaje {nivel}, no es válido')