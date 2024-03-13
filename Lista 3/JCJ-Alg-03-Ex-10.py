# Aluno: Jairo Caetano Junior
# Curso: Algoritmo - BCC - 1º Fase - 2024/01

posicao_no_tabuleiro = input("Informe a posição no tabuleiro: ").upper()

if posicao_no_tabuleiro[0] in 'ACEG' and int(posicao_no_tabuleiro[1]) in range(1, 9):
	if posicao_no_tabuleiro[0] in 'ACEG' and int(posicao_no_tabuleiro[1]) % 2 == 0:
		print("A casa é preta.")
	else:
		print("A casa é branca.")
elif posicao_no_tabuleiro[0] in 'BDF' and int(posicao_no_tabuleiro[1]) in range(1, 9):
	if posicao_no_tabuleiro[0] in 'BDF' and int(posicao_no_tabuleiro[1]) % 2 == 0:
		print("A casa é branca.")
	else:
		print("A casa é preta.")
else:
	print("A posição informada não é válida.")
