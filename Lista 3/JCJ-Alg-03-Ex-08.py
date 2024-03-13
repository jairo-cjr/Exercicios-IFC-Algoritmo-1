# Aluno: Jairo Caetano Junior
# Curso: Algoritmo - BCC - 1º Fase - 2024/01
import sys
'''
C4 261.63
D4 293.66
E4 329.63
F4 349.23
G4 392.00
A4 440.00
B4 493.88
'''

nota = input("Informe a nota musical: ").capitalize()

if nota[0] == 'C':
	freq = 261.63 / (2 ** (4 - int(nota[1])))
elif nota[0] == 'D':
	freq = 293.66 / (2 ** (4 - int(nota[1])))
elif nota[0] == 'E':
	freq = 329.63 / (2 ** (4 - int(nota[1])))
elif nota[0] == 'F':
	freq = 349.23 / (2 ** (4 - int(nota[1])))
elif nota[0] == 'G':
	freq = 392.00 / (2 ** (4 - int(nota[1])))
elif nota[0] == 'A':
	freq = 440.00 / (2 ** (4 - int(nota[1])))
elif nota[0] == 'B':
	freq = 493.88 / (2 ** (4 - int(nota[1])))
else:
	print("Nota inválida.")
	sys.exit()

print(f"A frequência da nota {nota} é de {freq:.2f}Hz.")
