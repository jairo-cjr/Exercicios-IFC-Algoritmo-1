# Aluno: Jairo Caetano Junior
# Curso: Algoritmo - BCC - 1º Fase - 2024/01
cents = int(input('Digite a quantidade de centavos: '))
cents_50 = cents // 50
cents = cents % 50
cents_25 = cents // 25
cents = cents % 25
cents_10 = cents // 10
cents = cents % 10
cents_5 = cents // 5
cents = cents % 5
cents_1 = cents // 1
cents = cents % 1

print(f'Troco\n{cents_50} moedas de 50 centavos\n{cents_25} moedas de 25 centavos\n{cents_10} moedas de 10 centavos\n{cents_5} moedas de 5 centavos\n{cents_1} moedas de 1 centavo')
