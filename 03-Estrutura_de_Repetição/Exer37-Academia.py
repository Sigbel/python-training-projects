"""
Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, 
a mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a cada um dos 
clientes da academia seu código, sua altura e seu peso. O final da digitação de dados deve ser 
dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar o programa também deve ser 
informados os códigos e valores do clente mais alto, do mais baixo, do mais gordo e do mais magro, 
além da média das alturas e dos pesos dos clientes
"""

num_cliente = int(input("Digite o número de clientes: "))

peso_maior = 0
peso_menor = 0
cod_peso_maior = 0 
cod_peso_menor = 0 

altura_maior = 0
altura_menor = 0
cod_altura_menor = 0
cod_altura_maior = 0
c = 0

for n in range(num_cliente):
    cod = int(input(f"Digite o código do {n+1}º cliente: "))
    altura = float(input(f"Digite a altura do {n+1}º cliente: "))
    peso = float(input(f"Digite o peso do {n+1}º cliente: "))
    while c < 1:
        peso_menor = peso
        cod_peso_menor = cod
        altura_menor = altura
        cod_altura_menor = cod
        c += 1
# Definição de peso maior
    if peso > peso_maior:
        peso_maior = peso
        cod_peso_maior = cod
# Definição de altura maior
    if altura > altura_maior:
        altura_maior = altura
        cod_altura_maior = cod
# Definição de peso menor
    if peso < peso_menor:
        peso_menor = peso
        cod_peso_menor = cod
# Definição de altura menor
    if altura < altura_menor:
        altura_menor = altura
        cod_altura_menor = cod
    print()

print("De acordo com as medidas temos: ")

print (f"Cliente mais alto: Código {cod_altura_maior} / Altura: {altura_maior} m")
print (f"Cliente mais baixo: Código {cod_altura_menor} / Altura: {altura_menor} m")
print (f"Cliente mais gordo: Código {cod_peso_maior} / Peso: {peso_maior} kg")
print (f"Cliente mais magro: Código {cod_peso_menor} / Peso: {peso_menor} kg")
