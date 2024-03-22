# Aluno: Jairo Caetano Junior
# Curso: Algoritmo - BCC - 1º Fase - 2024/01

N = int(input("Digite o valor de N: "))
A =1
i = 3

while i <= (2 * N - 1):
	A += 1 / i
	i += 2

print(f"O valor de A é {A}")

