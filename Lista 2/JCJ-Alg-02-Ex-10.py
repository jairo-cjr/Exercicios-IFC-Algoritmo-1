# Aluno: Jairo Caetano Junior
# Curso: Algoritmo - BCC - 1º Fase - 2024/01
matricula = int(input("Digite o número de matrícula do aluno: "))
year = matricula // 10000
semester = (matricula % 10000) // 1000
print(f"O aluno foi matriculado no ano {year} e no {semester}º semestre.")
