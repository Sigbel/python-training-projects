"""
Exercício 11 - Elementos Intercalados (2)

Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.
"""

vetor_1 = []
vetor_2 = []
vetor_3 = []
vetor_4 = []

for c1 in range(10):
    num = int(input(f"Digite {c1+1}º número do Vetor 1: "))
    vetor_1.append(num)

for c2 in range(10):
    num = int(input(f"Digite {c2+1}º número do Vetor 2: "))
    vetor_2.append(num)

for c3 in range(10):
    num = int(input(f"Digite {c3+1}º número do Vetor 2: "))
    vetor_2.append(num)

for c4 in range(len(vetor_1)):
    vetor_4.append(vetor_1[c4])
    vetor_4.append(vetor_2[c4])
    vetor_4.append(vetor_3[c4])

print(vetor_3)
