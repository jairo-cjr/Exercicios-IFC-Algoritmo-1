# Aluno: Jairo Caetano Junior
# Curso: Algoritmo - BCC - 1º Fase - 2024/01
# 130, 106, 70, 40

dB = int(input("Informe o nivel de barulho em decibéis: "))

if dB > 130:
	print("Nível de barulho maior que o de uma britadeira.")
elif dB > 106 and dB < 130:
	print("Nível de barulho está entre o de um cortador de grama e uma britadeira.")
elif dB > 70 and dB < 106:
	print("Nível de barulho está entre um despertador e um cortador de grama.")
elif dB > 40 and dB < 70:
	print("Nível de barulho está entre uma sala silenciosa e um despertador.")
elif dB == 130:
	print("Nível de barulho igual ao de uma britadeira.")
elif dB == 106:
	print("Nível de barulho igual ao de um cortador de grama.")
elif dB == 70:
	print("Nível de barulho igual ao de um despertador.")
elif dB == 40:
	print("Nível de barulho igual ao de uma sala silenciosa.")
else:
	print("Nível de barulho menor que o de uma sala silenciosa.")
