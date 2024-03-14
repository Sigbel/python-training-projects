"""
Exercício 26 - Posto de Gasolina

Um posto está vendendo combustíveis com a seguinte tabela de descontos:

* Álcool:
    - até 20 litros, desconto de 3% por litro
    - acima de 20 litros, desconto de 5% por litro
* Gasolina:
    - até 20 litros, desconto de 4% por litro
    - acima de 20 litros, desconto de 6% por litro

Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma:
A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é
R$ 2,50 o preço do litro do álcool é R$ 1,90.
"""

tipo = str(input("Insira o tipo de Combustível (A) - Álcool / (G) - Gasolina: ")).upper()
litros = int(input("Insira quantos litros deseja abastecer: "))
calculo = 0
desconto = 0

if tipo == "A":
    calculo = litros * 1.90
    if 0 < litros <= 20:
        desconto = (calculo * 0.03) * litros
    else:
        desconto = (calculo * 0.05) * litros
    print(f"O valor a ser pago é: R$ {calculo - desconto}")
elif tipo == "G":
    calculo = litros * 2.50
    if 0 < litros <= 20:
        desconto = (calculo * 0.04) * litros
    else:
        desconto = (calculo * 0.06) * litros
    print(f"O valor a ser pago é: R$ {calculo - desconto}")
else:
    print("Digite uma letra válida!")
