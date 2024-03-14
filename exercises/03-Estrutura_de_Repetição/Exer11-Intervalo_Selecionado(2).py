"""
Exercício  11 - Intervalo Selecionado (2)

Altere o programa anterior para mostrar no final a soma dos números.
"""

num_01 = int(input("Digite o 1º número: "))
num_02 = int(input("Digite o 2º número: "))
soma = 0
print()

print("O intervalo selecionado inclui os seguintes números: ")
for n in range(num_01,num_02+1):
    soma = n + soma
    print(n, end=" ")
print(f"\nA soma de todos os números do intervalo é: {soma}")
