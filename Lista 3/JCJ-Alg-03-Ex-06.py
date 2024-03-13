# Aluno: Jairo Caetano Junior
# Curso: Algoritmo - BCC - 1º Fase - 2024/01

lado_a = float(input("Informe o valor do lado A: "))
lado_b = float(input("Informe o valor do lado B: "))
lado_c = float(input("Informe o valor do lado C: "))

if (lado_a == lado_b) and (lado_b == lado_c):
	print("Triângulo Equilátero")
elif (lado_a != lado_b) and (lado_b != lado_c) and (lado_a != lado_c):
	print("Triângulo Escaleno")
else:
	print("Triângulo Isósceles")
