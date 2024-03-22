# Aluno: Jairo Caetano Junior
# Curso: Algoritmo - BCC - 1º Fase - 2024/01

N = int(input("Digite o valor de N: "))
A =1

for i in range(2, N+1):
	if i % 2 == 0:
		A -= 1 / i
	else:
		A += 1 / i

print(f"O valor de A é {A}")

