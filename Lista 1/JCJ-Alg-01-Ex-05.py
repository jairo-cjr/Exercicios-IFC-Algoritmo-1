# Aluno: Jairo Caetano Junior
# Curso: Algoritmo - BCC - 1º Fase - 2024/01
qtd_vasilhames_menores = int(input("Informe a quantidade de vasilhames de 1 litro ou menos: "))
qtd_vasilhames_maiores = int(input("Informe a quantidade de vasilhames de mais de 1 litro: "))
valor_total = (qtd_vasilhames_menores * 0.10) + (qtd_vasilhames_maiores * 0.25)
print(f"A quantidade de valor total a ser paga é de R${round(valor_total, 2)}!")
