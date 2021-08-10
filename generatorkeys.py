import random

minus = "abcdfghijklmnopqrstuvwxyz"
mayus = minus.upper()
numeros = "0123456789"
simbolos = "°!#$%&/()=?¡¿{*}>]<[-_"

base = minus+mayus+numeros+simbolos
longitud = int(input("Ingrese la cantidad de caracteres: "))

muestra = random.sample(base, longitud)
password = "".join(muestra)
print (password)