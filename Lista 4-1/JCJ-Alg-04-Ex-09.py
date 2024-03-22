# Aluno: Jairo Caetano Junior
# Curso: Algoritmo - BCC - 1º Fase - 2024/01

numeros = []
maior  = None
menor  = None
media  = 0

i = 1
while True:
	numero = input(f"Digite o {i}º número: ")
	if numero == "":
		break
	else:
		numeros.append(int(numero))
		i += 1

for i in range(0, numeros.__len__()):
	media += numeros[i]
	if maior is None or numeros[i] > maior:
		maior = numeros[i]
	if menor is None or numeros[i] < menor:
		menor = numeros[i]

print(f"O maior número é {maior}")
print(f"O menor número é {menor}")
print(f"A média dos números é {media/10}")
