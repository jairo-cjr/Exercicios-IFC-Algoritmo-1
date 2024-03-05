# Aluno: Jairo Caetano Junior
# Curso: Algoritmo - BCC - 1º Fase - 2024/01

valor_inicial = float(input("Inform a quantia inicial a ser depositada: "))

print(f"O valor total no primeiro ano com juros será de: R${round(valor_inicial * (1 + 0.12) ** (1 * 1), 2)}")
print(f"O valor total no segundo ano com juros será de: R${round(valor_inicial * (1 + 0.12) ** (1 * 2), 2)}")
print(f"O valor total no terceiro ano com juros será de: R${round(valor_inicial * (1 + 0.12) ** (1 * 3), 2)}")
