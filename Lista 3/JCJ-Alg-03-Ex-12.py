# Aluno: Jairo Caetano Junior
# Curso: Algoritmo - BCC - 1º Fase - 2024/01

# Ano bissexto

ano = int(input("Informe o ano: "))

if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
	print(f"O ano {ano} é bissexto.")
else:
	print(f"O ano {ano} não é bissexto.")
