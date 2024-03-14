"""
Exercício 43 - Cardápio da Lanchonete

O cardápio de uma lanchonete é o seguinte:

Especificação   Código  Preço

Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00

Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre 
o valor a ser pago por item (preço * quantidade) e o total geral do pedido. Considere que o cliente 
deve informar quando o pedido deve ser encerrado.
"""

soma_100 = 0
soma_101 = 0
soma_102 = 0
soma_103 = 0
soma_104 = 0
soma_105 = 0
c_100 = 0
c_101 = 0
c_102 = 0
c_103 = 0
c_104 = 0
c_105 = 0

while True:
    cod = int(input("Digite o código do item: "))
    while cod != 0 and (cod < 100 or cod > 105):
        cod = int(input("Digite o código correto: "))
    if cod == 0:
        break
    quantidade = int(input("Digite a quantidade desejada: "))
    if cod == 100:
        calculo = quantidade * 1.2
        soma_100 = calculo + soma_100
        c_100 += quantidade
    elif cod == 101:
        calculo = quantidade * 1.3
        soma_101 = calculo + soma_101
        c_101 += quantidade
    elif cod == 102:
        calculo = quantidade * 1.5
        soma_102 = calculo + soma_102
        c_102 += quantidade
    elif cod == 103:
        calculo = quantidade * 1.2
        soma_103 = calculo + soma_103
        c_103 += quantidade
    elif cod == 104:
        calculo = quantidade * 1.3
        soma_104 = calculo + soma_104
        c_104 += quantidade
    elif cod == 105:
        calculo = quantidade * 1
        soma_105 = calculo + soma_105
        c_105 += quantidade

soma_total = soma_100+soma_101+soma_102+soma_103+soma_104+soma_105

print(" TOTAL DE ITENS ".center(58,"-"))
print()
print(f"Cachorro Quente".ljust(17), f"| QTDE: {c_100}".ljust(12), f"| Valor Pago: R$", f"{soma_100:.2f}".rjust(10))
print(f"Bauro Simples".ljust(17), f"| QTDE: {c_101}".ljust(12), f"| Valor Pago: R$", f"{soma_101:.2f}".rjust(10))
print(f"Bauro com ovo".ljust(17), f"| QTDE: {c_102}".ljust(12), f"| Valor Pago: R$", f"{soma_102:.2f}".rjust(10))
print(f"Hambúrguer".ljust(17), f"| QTDE: {c_103}".ljust(12), f"| Valor Pago: R$", f"{soma_103:.2f}".rjust(10))
print(f"Cheeseburguer".ljust(17), f"| QTDE: {c_104}".ljust(12), f"| Valor Pago: R$", f"{soma_104:.2f}".rjust(10))
print(f"Refrigerante".ljust(17), f"| QTDE: {c_105}".ljust(12), f"| Valor Pago: R$", f"{soma_105:.2f}".rjust(10))
print()

print(f"Total Geral: R$ {soma_total:.2f}")
