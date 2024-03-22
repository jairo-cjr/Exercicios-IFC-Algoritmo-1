# Aluno: Jairo Caetano Junior
# Curso: Algoritmo - BCC - 1º Fase - 2024/01

numeros = []
maior  = None
menor  = None
media  = 0

for i in range(0, 10):
	numeros.append(int(input(f"Digite o {i+1}º número: ")))

for i in range(0, 10):
	media += numeros[i]
	if maior is None or numeros[i] > maior:
		maior = numeros[i]
	if menor is None or numeros[i] < menor:
		menor = numeros[i]

print(f"O maior número é {maior}")
print(f"O menor número é {menor}")
print(f"A média dos números é {media/10}")
