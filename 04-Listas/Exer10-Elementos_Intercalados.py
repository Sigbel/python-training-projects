"""
Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores 
deverão ser compostos pelos elementos intercalados dos dois outros vetores.
"""

vetor_1 = []
vetor_2 = []
vetor_3 = []

for c1 in range(10):
    num = int(input(f"Digite {c1+1}º número do Vetor 1: "))
    vetor_1.append(num)

for c2 in range(10):
    num = int(input(f"Digite {c2+1}º número do Vetor 2: "))
    vetor_2.append(num)

for c3 in range(len(vetor_1)):
    vetor_3.append(vetor_1[c3])
    vetor_3.append(vetor_2[c3])

print(vetor_3)
