
def ejerccio1():
    contraseña = input("Ingrese una contraseña: ")
    contraseña_encriptada = ""
    for caracter in contraseña:
        contraseña_encriptada = contraseña_encriptada + "*"
    return contraseña_encriptada
print(ejerccio1())
