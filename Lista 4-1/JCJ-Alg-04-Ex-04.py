# Aluno: Jairo Caetano Junior
# Curso: Algoritmo - BCC - 1º Fase - 2024/01

N = int(input("Informe o valor de N: "))
A = 1
for i in range(2, N+1):
    A += 1 / i

print(f"A = {A:.2f}")
