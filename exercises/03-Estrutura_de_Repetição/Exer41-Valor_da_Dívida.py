"""
Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: 
valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.

Os juros e a quantidade de parcelas seguem a tabela abaixo:

Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
1       0
3       10
6       15
9       20
12      25
_________________________________________________________________________
Exemplo de saída do programa:
Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
R$ 1.000,00     0               1                       R$  1.000,00
R$ 1.100,00     100             3                       R$    366,00
R$ 1.150,00     150             6                       R$    191,67
"""

valor_divida = float(input("Digite o valor da dívida: "))

print("Valor da Divida".ljust(20), end="|")
print("Juros".ljust(7), end="|")
print("QTDE. Parcelas".ljust(15), end="|")
print("Valor da Parcela".ljust(16))

print(f"R$ {valor_divida:.2f}".ljust(20), f"0".ljust(7), f"1".ljust(15), f"R$".ljust(2), f"{valor_divida:.2f}".rjust(13))
juros = 10
parcelas = 3


for n in range(4):
    print(f"R$ {valor_divida+(valor_divida*(juros/100)):.2f}".ljust(20), f"{valor_divida*(juros/100):.0f}".ljust(7), f"{parcelas}".ljust(15), 
    f"R$".ljust(2), f"{(valor_divida+(valor_divida*(juros/100)))/parcelas:.2f}".rjust(13))
    juros += 5
    parcelas += 3

