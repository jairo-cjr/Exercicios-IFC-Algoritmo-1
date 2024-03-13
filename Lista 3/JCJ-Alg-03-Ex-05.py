# Aluno: Jairo Caetano Junior
# Curso: Algoritmo - BCC - 1º Fase - 2024/01

mes = input("Informe o nome do mês: ").capitalize()

if mes in ("JaneiroMarcoMaioJulhoAgostoOutubroDezembro"):
	print(f"{mes} tem 31 dias")
elif mes in ("AbrilJunhoSetembroNovembro"):
	print(f"{mes} tem 30 dias")
elif mes == "Fevereiro":
	print(f"{mes} tem 28 ou 29 dias")
else:
	print("Mês inválido.")
