#Hallar la hipotenusa de un tríangulo

import math

catetoa = int(input("Ingrese valor catetoa: \n"))
catetob = int(input("Ingrese valor catetob: \n"))

raiz_cuadrada = math.sqrt(catetoa**2 + catetob**2)

print(raiz_cuadrada)