# Aluno: Jairo Caetano Junior
# Curso: Algoritmo - BCC - 1º Fase - 2024/01

dia = int(input("Informe o dia: "))
mes = input("Informe o mês: ").capitalize()

if dia == 1 and mes == 'Janeiro':
	print("Confraternização universal")
elif dia == 21 and mes == 'Abril':
	print("Tiradentes")
elif dia == 1 and mes == 'Maio':
	print("Dia do trabalho")
elif dia == 7 and mes == 'Setembro':
	print("Independência do Brasil")
elif dia == 12 and mes == 'Outubro':
	print("Nossa Senhora Aparecida")
elif dia == 2 and mes == 'Novembro':
	print("Finados")
elif dia == 15 and mes == 'Novembro':
	print("Proclamação da República")
elif dia == 25 and mes == 'Dezembro':
	print("Natal")
else:
	print("A data informada não é um feriado nacional.")
