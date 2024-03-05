# Aluno: Jairo Caetano Junior
# Curso: Algoritmo - BCC - 1º Fase - 2024/01
valor_prato_principal = float(input("Informe o valor do prato principal: "))
valor_suco = float(input("Informe o valor do suco: "))
valor_sobremesa = float(input("Informe o valor da sobremesa: "))
taxa_servico = (valor_prato_principal + valor_suco + valor_sobremesa) * 0.10
valor_total = valor_prato_principal + valor_suco + valor_sobremesa + taxa_servico
print(f"O valor total a ser pago é de R${round(valor_total, 2)}")
