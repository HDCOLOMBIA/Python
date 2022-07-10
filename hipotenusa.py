#Hallar la hipotenusa de un tríangulo

import math
from math import sqrt

catA = float(input("Ingrese valor cateto A: " + "\n"))
catB = float(input("Ingrese valor cateto B: " + "\n"))

hipotenusa = sqrt(catA**2 + catB**2)

print(f"El valor de la hipotenusa del tríangulo es: \n {hipotenusa}")

