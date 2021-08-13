'''
list = ["lunes","martes","miercoles","jueves","viernes"]
initial = int(input("Ingrese número de la semana inicial: "))
end = int(input("Ingrese número final del semana: "))
print(list[initial:end])
'''
'''
lista = [1,2,4,5,6,7,8,9,10]
indice = int(input("Ingrese el apendice donde desea agregar el valor: "))
valor = int(input("Ingrese el valor que desea agregar: "))
#lista.extend: La función extend agrega números al final
lista.insert(indice, valor)
print(lista)
'''

'''
lista = [1,2,4,5,6,7,8,9,10]
#saber si hay X elemento en una lista
print(10 in lista)
'''

'''
lista = [1,2,4,5,6,7,8,9,10]
#contar sobre la lista
print(lista.count(11))
'''

'''
lista = [1,2,4,5,6,7,8,9,10]
#eliminar
lista.pop()
print(lista)
'''
'''
lista = [1,2,4,5,6,7,8,9,10]
#eliminar
lista.remove()
print(lista)
'''

'''
lista = [1,2,4,5,6,7,8,9,10]
#limpiar la lista
lista.clear()
print(lista)
'''

'''
#multiplicar la lista
lista = [1,2,3,4,5,6,7,8,9,10]*3
print(lista)
'''


