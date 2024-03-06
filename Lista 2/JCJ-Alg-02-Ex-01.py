# Aluno: Jairo Caetano Junior
# Curso: Algoritmo - BCC - 1º Fase - 2024/01

day = int(input("Digite o numero de dias: "))
time = input("Digite as horas, minutos e segundos no forma HH:MM:SS: ").split(':')
total_seconds = (int(time[0]) * 3600) + (int(time[1]) * 60) + int(time[2]) + (day * 86400)

print(f"O total do intervalo é de {total_seconds} segundos.")
