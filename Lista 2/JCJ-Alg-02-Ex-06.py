# Aluno: Jairo Caetano Junior
# Curso: Algoritmo - BCC - 1º Fase - 2024/01
number = int(input("Digite um número de 4 dígitos: "))
first_digit = number // 1000
second_digit = (number % 1000) // 100
third_digit = (number % 100) // 10
fourth_digit = number % 10
sum_digits = first_digit + second_digit + third_digit + fourth_digit
print(f"A soma dos dígitos do número {number} é {sum_digits}")
