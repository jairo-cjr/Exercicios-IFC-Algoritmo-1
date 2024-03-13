# Aluno: Jairo Caetano Junior
# Curso: Algoritmo - BCC - 1º Fase - 2024/01

idade_cachorro = int(input("Informe a idade do cachorro em anos: "))
idade_humano = None;

if idade_cachorro  <= 2 and idade_cachorro > 0:
	idade_humano = idade_cachorro * 10.5
	print(f"A idade do cachorro em anos humanos é: {idade_humano} anos")
elif idade_cachorro > 2:
	idade_humano =  21 + (idade_cachorro - 2) * 4
	print(f"A idade do cachorro em anos humanos é: {idade_humano} anos")
elif idade_cachorro == 0:
	idade_humano = 0
	print(f"A idade do cachorro em anos humanos é: {idade_humano} ano")
else:
	print("Idade inválida")
