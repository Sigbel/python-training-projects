"""
O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um 
conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas 
informadas, bem como a média das temperaturas.
"""

menor = 0
maior = 0
soma = 0
c = 0
c_temp = 0

print()
while True:
    temp = int(input(f"Digite o valor da {c_temp+1}ª temperatura: "))
    c_temp += 1
    while c < 1:
        menor = temp
        c += 1
    if temp > maior:
        maior = temp
    if temp < menor:
        menor = temp
    soma = soma + temp
    continua = int(input("Digite '0' para sair ou '1' para continuar: "))
    while continua != 0 and continua != 1:
        continua = int(input("Favor digitar somente 0 ou 1.\nTente novamente: "))
    if continua == 0:
        break
    else:
        continue
    
print()
print(f"A maior temperatura é: {maior}\nA menor temperatura é: {menor}\nA média de todos as temperaturas é: {soma/c_temp:.2f}")
