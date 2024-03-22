# Aluno: Jairo Caetano Junior
# Curso: Algoritmo - BCC - 1º Fase - 2024/01

N = int(input("Informe o valor de N: "))
A = N
i = 1
while N >= 1:
	print(f"{N} - {i} / {i+1} = {(N - i )/( i + 1)}")
	A += (N - i) / (i + 1)
	N -= i
	i += 1

print(f"A = {A:.2f}")

