"""
Exercício 8 - Salário do Mês

Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
"""

hora = float(input("Digite o valor referente a hora trabalhada: "))
horas_mes = float(input("Digite a quantidade de horas trabalhadas no mês: "))
calculo = hora * horas_mes

print(f"O total ganho no mês foi: {calculo}")