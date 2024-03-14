"""
Exercício 29 - Peso Excedente

João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de
R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.
Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as
mensagens adequadas.
"""

peso = float(input("Digite o peso do peixe: "))

if (peso > 50):
    excesso = peso - 50
    multa = excesso * 4

    print(f"O peixe pescado tem: {peso} kg \nO excesso foi de: {excesso} kg \nE a multa foi de: R$ {multa}")
else:
    print("Peso não ultrapassou o limite estabelecido")
