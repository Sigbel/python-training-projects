"""
Exercício 12 - Desconto de IR

Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e
3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto
menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
    - Salário Bruto até 900 (inclusive) - isento
    - Salário Bruto até 1500 (inclusive) - desconto de 5%
    - Salário Bruto até 2500 (inclusive) - desconto de 10%
    - Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de
    hora é 220.
"""

valor_hora = float(input("Digite o valor ganho por hora: "))
quantidade_hora = float(input("Digite o quantidade de horas trabalhadas: "))
salario_bruto = valor_hora * quantidade_hora
novo_salario = salario_bruto
desc_salario = 0
ir = 0
inss = salario_bruto * 0.1
fgts = salario_bruto * 0.11

if 900 < novo_salario <= 1500:
    ir = novo_salario * 0.05
if 1500 < novo_salario <= 2500:
    ir = novo_salario * 0.1
if novo_salario > 2500:
    ir = novo_salario * 0.2

print(f"Salário Bruto: R$ {salario_bruto}")
print(f"(-) IR: R$ {ir:.2f}")
print(f"(-) INSS: R$ {inss:.2f}")
print(f"FGTS: R$ {fgts:.2f}")
print(f"Total de Descontos: R$ {ir + inss:.2f}")
print(f"Salário líquido: R$ {salario_bruto - ir - inss}")
