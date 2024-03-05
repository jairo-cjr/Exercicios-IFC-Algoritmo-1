# Aluno: Jairo Caetano Junior
# Curso: Algoritmo - BCC - 1º Fase - 2024/01

import math

l = float(input("Informe o comprimento dos lados: "))
n = int(input("Informe o número de lados: "))

print(f"A area do poligono é: {round((n * l**2) / (4 * math.tan(math.pi / n)),2)}")
