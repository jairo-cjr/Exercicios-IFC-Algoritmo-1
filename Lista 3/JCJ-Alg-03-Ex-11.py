# Aluno: Jairo Caetano Junior
# Curso: Algoritmo - BCC - 1º Fase - 2024/01

a = float(input("Informe o valor de a: "))
b = float(input("Informe o valor de b: "))
c = float(input("Informe o valor de c: "))
delta = (b ** 2) - (4 * a * c)

if delta < 0:
	print("A equação não possui raízes reais.")
elif delta == 0:
	raiz = (-b) / (2 * a)
	print(f"A equação possui uma raiz real: {raiz}.")
else:
	raiz1 = (-b + (delta ** 0.5)) / (2 * a)
	raiz2 = (-b - (delta ** 0.5)) / (2 * a)
	print(f"A equação possui duas raízes reais: {raiz1:.2f} e {raiz2:.2f}.")
