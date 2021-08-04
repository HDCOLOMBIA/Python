# pedir nombre del usuario
name = str(input("Enter your name: "))
print("¡Hello " + name + "!")

#Pedir edad
age = int(input("Enter your age: "))
if age >= 18:
    print("Usted es mayor de edad")
if age <= 17:
    print("Usted es menor de edad")

#Ciclo para imprimir la edad
for i in range(age):
    print(name + " ha cumplido " + str(i+1) +" años")

#ingresar notas
Nota1 = float(input("Enter your note1: "))
Nota2 = float(input("Enter your note2: "))
Nota3 = float(input("Enter your note3: "))
promedio = float(Nota1 + Nota2 + Nota3)/3
print("su promedio es: " + str(promedio))

#Sacar el promedio
if promedio >= float(3):
    print("aprobado")
if promedio <= float(3):
    print("reprobado")
pass

#fin