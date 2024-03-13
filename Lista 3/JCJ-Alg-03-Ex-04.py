# Aluno: Jairo Caetano Junior
# Curso: Algoritmo - BCC - 1º Fase - 2024/01

lados = int(input("Informe a quantidade de lados do polígono: "))

if lados == 3:
	print("Triângulo")
elif lados == 4:
	print("Quadrilátero")
elif lados == 5:
	print("Pentágono")
elif lados == 6:
	print("Hexágono")
elif lados == 7:
	print("Heptágono")
elif lados == 8:
	print("Octógono")
elif lados == 9:
	print("Eneágono")
elif lados == 10:
	print("Decágono")
else:
	print("Numero de lados invalido.")

