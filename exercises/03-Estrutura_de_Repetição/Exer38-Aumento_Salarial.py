"""
Exercício 38 - Aumento de Salário

Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:

A. Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;

B. Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;

C. A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual 
do ano anterior. Faça um programa que determine o salário atual desse funcionário. Após concluir 
isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.
"""

valor_inicial = float(input("Digite o salário do funcionário em 1995: "))
ano_atual = int(input("Digite o ano atual: "))
reajuste = 0.015
valor_atual = 0

for n in range((ano_atual-1995)+1):
    valor_atual = valor_inicial + (valor_inicial*reajuste)
    valor_inicial = valor_atual
    reajuste = reajuste * 2

print(f"Salário em {ano_atual}: R$ {valor_atual:.2f}")
