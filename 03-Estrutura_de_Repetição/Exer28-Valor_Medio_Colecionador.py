"""
Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e 
o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para
em cada um.
"""

num_cds = int(input("Digite a quantidade de CDs adquiridos: "))
soma = 0

for n in range(num_cds):
    valor = float(input(f"Digite o valor gasto {n+1}º CD: "))
    soma = soma + valor

print(f"O valor total gasto foi R$ {soma}\nA média de gasto por CD foi R$ {soma/num_cds}")
