'''
Construir un programa que simule el funcionamiento de una calculadora que puede realizar
las cuatro operaciones aritméticas básicas (suma, resta, multiplicación y división).
El usuario debe especificar la operación con el primer carácter  del nombre de la operación.

S, s – Suma
R, r – Resta
P, p, M, m – Multiplicación
D, d - División
'''

#calculadora


valor1 = int(input("Ingrese el primero valor: "))
valor2 = int(input("Ingrese el segundo valor: "))
operacion = input("Ingrese una letra en relación a la operación: (S,s - Suma) (R, r – Resta) (P, p, M, m – Multiplicación) (D, d - División) ").upper()
if operacion == 'S':
    resultado = valor1 + valor2
    print("El resultado de la suma es: ",resultado)
elif operacion == 'R':
    resultado = valor1 - valor2
    print("El resultado de la resta es: ",resultado)
elif operacion == 'P':
    resultado = valor1 * valor2
    print("El resultado de la multiplicacion es: ",resultado)
elif operacion == 'D':
    resultado = valor1 // valor2
    print("El resultado de la division es: ",resultado)
else:
    pass


