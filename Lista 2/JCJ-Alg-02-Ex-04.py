# Aluno: Jairo Caetano Junior
# Curso: Algoritmo - BCC - 1º Fase - 2024/01
num_1 = int(input('Digite o primeiro número: '))
num_2 = int(input('Digite o segundo número: '))
num_3 = int(input('Digite o terceiro número: '))

min_num = min(num_1, num_2, num_3)
max_num = max(num_1, num_2, num_3)
mid_num = num_1 + num_2 + num_3 - min_num - max_num

print(f'Os números em ordem crescente são: {min_num}, {mid_num} e {max_num}')
