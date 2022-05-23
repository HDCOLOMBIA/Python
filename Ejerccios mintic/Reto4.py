from sys import setrecursionlimit
import json
from pprint import print

catologo = input("")
data = json.loads(catologo)

servicios = input("")

listaServicios = servicios.split()

serSolicitado = []
valorSer = []
valorTotal = []

for j in  listaServicios:
    if j in data:
        valorSer.append(data[j])
        valorTotal = sum(valorSer)
        serSolicitado.append(j)

print(valorTotal)
print("".join(serSolicitado))