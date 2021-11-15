"""
A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz 
de gerar a série até o n−ésimo termo.
"""

ultimo_termo = int(input("Digite o n-ésimo termo da sequência de Fibonacci: "))
termo_1 = 1
termo_2 = 1
soma = 0

print(f"Sequência: {termo_1}, {termo_2}",end=" ")
for n in range(ultimo_termo-2):
    soma = termo_1 + termo_2
    termo_1 = termo_2
    termo_2 = soma
    print(f", {soma}",end=" ")
