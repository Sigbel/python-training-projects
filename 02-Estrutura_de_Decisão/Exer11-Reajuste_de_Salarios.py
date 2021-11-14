"""
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
    Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
        - salários até R$ 280,00 (incluindo) : aumento de 20%
        - salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
        - salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
        - salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
        o salário antes do reajuste;
        o percentual de aumento aplicado;
        o valor do aumento;
        o novo salário, após o aumento.
"""

salario = float(input("Digite o salário do colaborador: "))
salarioreaj = salario
novo_salario = 0
percentual = 0

if salarioreaj <= 280:
    salarioreaj = salarioreaj * 0.2
    novo_salario = salarioreaj + salario
    percentual = 0.2 * 100
elif 280 < salarioreaj < 700:
    salarioreaj = salarioreaj * 0.15
    novo_salario = salarioreaj + salario
    percentual = 0.15 * 100
elif 700 <= salarioreaj < 1500:
    salarioreaj = salarioreaj * 0.1
    novo_salario = salarioreaj + salario
    percentual = 0.1 * 100
elif salarioreaj >= 1500:
    salarioreaj = salarioreaj * 0.05
    novo_salario = salarioreaj + salario
    percentual = 0.05 * 100

print(f"O salário antes do reajuste era: R$ {salario}")
print(f"O percentual de reajuste é: {percentual}%")
print(f"O Valor do aumento é: R$ {salarioreaj}")
print(f"O novo salário será: R$ {novo_salario}")