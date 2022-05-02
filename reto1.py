pesochavo = int(input())
pesoquico = int((pesochavo+2)+4)
pesonono = int((pesochavo+pesoquico)/5)

print(pesochavo,pesoquico,pesonono)

if pesonono >= 0 and pesonono <= 20:
    print("uno")
elif pesonono > 20 and pesonono <= 40:
    print("dos")
elif pesonono > 40 and pesonono <= 80:
    print("tres")
elif pesonono > 80:
    print("cuatro")
