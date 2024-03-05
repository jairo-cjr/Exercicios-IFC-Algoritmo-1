# Aluno: Jairo Caetano Junior
# Curso: Algoritmo - BCC - 1º Fase - 2024/01

import math

t1 = math.radians(float(input("Informe a latitude 1: ")))
g1 = math.radians(float(input("Informe a longitude 1: ")))
t2 = math.radians(float(input("Informe a latitude 2: ")))
g2 = math.radians(float(input("Informe a longitude 2: ")))

distancia = 6371.01 * math.acos((math.sin(t1)*math.sin(t2)) + (math.cos(t1)*math.cos(t2 )) * math.cos(g1-g2))

print(f"A distância entre os dois pontos é de {round(distancia, 2)}Km")
