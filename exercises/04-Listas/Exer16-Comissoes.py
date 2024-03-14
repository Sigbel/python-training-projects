"""
Exercício 16 - Comissões

Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões. 
O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, um vendedor 
que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470. 
Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos 
seguintes intervalos de valores:

$200 - $299
$300 - $399
$400 - $499
$500 - $599
$600 - $699
$700 - $799
$800 - $899
$900 - $999
$1000 em diante

Desafio: Crie ma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados.
"""

contadores = [0,0,0,0,0,0,0,0,0,0]
calculos = [list(range(200,300)), list(range(300,400)), list(range(400,600)), list(range(600,700)), 
list(range(800,900)), list(range(900,1000))]

c = 0
while True:

    venda = float(input(f"Digite venda bruta da semana do {c+1}º vendedor: "))
    if venda == -1:
        break
    calculo_certo = (200+(venda*0.09))//1

    for c1 in range(2):
        for c2 in calculos[c1]:
            if calculo_certo == c2:
                contadores[c1] += 1
    if calculo_certo > 1000:
        contadores[9] += 1
    c += 1

print(f'Sálario (R$ 200 - R$ 299) = {contadores[0]}')
print(f'Sálario (R$ 300 - R$ 399) = {contadores[1]}')
print(f'Sálario (R$ 400 - R$ 499) = {contadores[2]}')
print(f'Sálario (R$ 500 - R$ 599) = {contadores[3]}')
print(f'Sálario (R$ 600 - R$ 699) = {contadores[4]}')
print(f'Sálario (R$ 700 - R$ 799) = {contadores[5]}')
print(f'Sálario (R$ 800 - R$ 899) = {contadores[6]}')
print(f'Sálario (R$ 900 - R$ 999) = {contadores[7]}')
print(f'Sálario (> R$ 1000)       = {contadores[8]}')
