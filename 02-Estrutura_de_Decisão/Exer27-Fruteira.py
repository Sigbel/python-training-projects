"""
Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto
de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças
adquiridas e escreva o valor a ser pago pelo cliente.
"""

kg_morango = float(input("Digite quantos quilos de morango o cliente comprou: "))
kg_maca = float(input("Digite quantos quilos de maça o cliente comprou: "))
soma_pesos = kg_morango + kg_maca
calculo_morango = 0
calculo_maca = 0

# Calculo para morango
if 0 < kg_morango <= 5:
    calculo_morango = kg_morango * 2.5
else:
    calculo_morango = kg_morango * 2.2

# Calculo para Maça
if 0 < kg_maca <= 5:
    calculo_maca = kg_maca * 1.8
else:
    calculo_maca = kg_maca * 1.5
valor_final = calculo_morango + calculo_maca

if soma_pesos > 8 or valor_final > 25:
    valor_final = valor_final - (valor_final*0.1)
print(f"O valor a ser pago é: R$ {valor_final}")