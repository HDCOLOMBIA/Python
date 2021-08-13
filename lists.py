'''
list = ["lunes","martes","miercoles","jueves","viernes"]
initial = int(input("Ingrese número de la semana inicial: "))
end = int(input("Ingrese número final del semana: "))
print(list[initial:end])
'''

lista = [1,2,4,5,6,7,8,9,10]
indice = int(input("Ingrese el apendice donde desea agregar el valor: "))
valor = int(input("Ingrese el valor que desea agregar: "))
lista.insert(indice, valor)
print(lista)
