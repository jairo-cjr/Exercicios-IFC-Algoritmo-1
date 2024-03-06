# Aluno: Jairo Caetano Junior
# Curso: Algoritmo - BCC - 1º Fase - 2024/01

seconds = int(input('Digite a quantidade de segundos: '))
days = seconds // 86400
hours = (seconds % 86400) // 3600
minutes = (seconds % 3600) // 60
seconds = seconds % 60

print(f"{days:02} dias e {hours:02}:{minutes:02}:{seconds:02}")
