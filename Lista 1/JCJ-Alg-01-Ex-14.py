# Aluno: Jairo Caetano Junior
# Curso: Algoritmo - BCC - 1º Fase - 2024/01
import math

lado_1 = float(input("Informe o valor do lado 1: "))
lado_2 = float(input("Informe o valor do lado 2: "))
lado_3 = float(input("Informe o valor do lado 3: "))

l = (lado_1 + lado_2 + lado_3) / 2

print(f"A área do triângulo é {round(math.sqrt(l * (l - lado_1) * (l - lado_2) * (l - lado_3)), 2)}")
