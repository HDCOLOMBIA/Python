def nota_quices(codigo: str, nota1: int, nota2: int, nota3: int, nota4: int, nota5: int) -> str:
    promedio = min(nota1, nota2,  nota3,  nota4, nota5)
    promedio = ((nota1 + nota2 + nota3 + nota4 + nota5) - promedio) / 4 * 5 / 100
    promedio = round(promedio, 2)
    return (f"El promedio del estudiante {codigo} es: {promedio}")

print(nota_quices("AA0010276", 40, 50, 39, 76, 96))