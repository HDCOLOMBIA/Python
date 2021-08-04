'''
Escribir un programa que pregunte el nombre del usuario en la consola y
después de que el usuario lo introduzca muestre por pantalla la cadena
¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido.
name = str(input("Enter your name: "))
print("¡Hola " + name + "!")
'''

'''
Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
age = int(input("Enter your age: "))
if age >= 18:
    print("Usted es mayor de edad")
if age <= 17:
    print("Usted es menor de edad")
'''

'''
Por favor realizar un programa que realice el promedio de un estudiante e imprimir su resultado

Pitas:
Nota1
nota2
nota3
promedio

Nota1 = float(input("Enter your note1: "))
Nota2 = float(input("Enter your note2: "))
Nota3 = float(input("Enter your note3: "))
promedio = float(Nota1 + Nota2 + Nota3)/3
print("su promedio es: " + str(promedio))
'''


'''
Utilizar el programa de notas y adicionar sentencias para dar un mensaje de aprobado o reprobado, según estos valores para

Reprobado: Menos de 3
Aprobado: más de 3

Pistas:
Nota1
nota2
nota3
promedio

if promedio >= float(3):
    print("aprobado")
if promedio <= float(3):
    print("reprobado")
'''

'''
Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
Pistas:
age
for i in range
+ str(i+1) +

age = int(input("Enter your age: "))
for i in range(age):
    print("Usted ha cumplido " + str(i+1) +" años")
'''




