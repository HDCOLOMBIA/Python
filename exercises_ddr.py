# 2) Crear dos variables numéricas, sumarlas y mostrar el resultado
# num1 = int(5)
# num2 = int(6)
# sum = int(num1 + num2)
# print(f"El total de la suma es: {sum}")

# 3) Mostrar el precio del IVA de un producto con un valor de 100 y su precio final.
# producto = int(100)
# iva_col = int((producto*19)/100)
# print(f"El precio del prodcto es {producto} IVA del producto es de: {iva_col} dolares")

# 4) De dos números, saber cual es el mayor.
# num1 = int(input("Ingrese primer numéro entero: "))
# num2 = int(input("Ingrese segundo numéro entero: "))
# if num1 > num2:
#     print(f"El número {num1} es mayor que {num2}")
# else:
#     print(f"El número {num1} es menor que {num2}")

# 5) Crea una variable numérica y si esta entre 0 y 10, mostrar un mensaje indicándolo.
# varnum = int(input("Ingresar un número entero: "))
# if varnum >= 0 and varnum <= 10:
#     print(f"El número {varnum} que ingreso esta dentro del rango de 0 a 10")
# else:
#     print(f"El número {varnum} no esta en el rango de 0 a 10")

# 6) Añadir al anterior ejercicio, que si esta entre 11 y 20, muestre otro mensaje diferente y si esta entre 21 y 30 otro mensaje.
# varnum = int(input("Ingresar un número entero: "))
# if varnum >= 0 and varnum <= 10:
#     print(f"El número {varnum} que ingreso esta dentro del rango de 0 a 10")
# elif varnum >= 11 and varnum <= 20:
#     print(f"El número {varnum} esta en el rango de 11 a 20")
# elif varnum >= 21 and varnum <= 30:
#     print(f"El número {varnum} esta en el rango de 21 a 30")
# else:
#     print(f"El número {varnum} no esta en ninguno de los rangos anteriores")

# # 7) Mostrar con un while los números del 1 al 100.
# num = 0
# while num < 100:
#     print(str(num))
#     num += 1

# print("Fin del bucle")

# 8) Mostrar con un for los números del 1 al 100.
# num = 0
# for num in range(100):
#     print(num)
#     num += 1

# print("Fin del bucle")

# 9) Mostrar los caracteres de la cadena “Hola mundo”.

# ejemplo original
# for i in "Hola mundo":
#     print(i)

# text = str(input("Introduza un texto: "))
# for i in text:
#     print(i)

# 10) Mostrar los números pares entre 1 al 100.
# 1º forma
# print("1 forma")
# for i in range(1,101):
#     if( (i%2)==0 ):
#         print(i)

# print("")

# 2º forma
# print("2 forma")
# for i in range(2,101,2):
#     print(i)

# 11) Generar un rango entre 0 y 10
# ejemplo ddr
# rango = list( range(10) )
# print(rango)

# Mi código
# rango =  int(input("Introduza un rango: "))
# print(list(range(int(rango))))

# 12) Generar un número entre 5 y 10

# rango = list(range(5,10))
# ejemplo ddr
# print(rango)

# MI código
# print(list(range(5,11)))

# 13) Generar un rango de 10 a 0.
# rango = list(range(10,0,-1))
# print(rango)

# My code
# print(list(range(10,0,-1)))

# 14) Generar un rango de 0 a 10 y de 15 a 20, incluidos el 10 y 20
# rango1 = list(range(0,11))
# rango2 = list(range(15,21))
# final = rango1 + rango2
# print(final)