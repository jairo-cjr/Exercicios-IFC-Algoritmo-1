# Aluno: Jairo Caetano Junior
# Curso: Algoritmo - BCC - 1º Fase - 2024/01

qtd_bugigangas = int(input("Informe a quantidade de bugigangas: "))
qtd_quinquilharias = int(input("Informe a quantidade de quinquilharias: "))
print(f"O peso total do pedido é de {(qtd_bugigangas * 75) + (qtd_quinquilharias * 112)} gramas / {round(((qtd_bugigangas * 75) + (qtd_quinquilharias * 112)) / 1000, 2)} Kg.")
