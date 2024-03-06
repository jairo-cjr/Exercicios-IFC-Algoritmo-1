# Aluno: Jairo Caetano Junior
# Curso: Algoritmo - BCC - 1º Fase - 2024/01
date = int(input("Digite uma data no formato DDMMAAAA: "))
day = date // 1000000
month = (date % 1000000) // 10000
year = date % 10000
print(f"A data {date:08} no formato AAAAMMDD é: {year:04}{month:02}{day:02}")
