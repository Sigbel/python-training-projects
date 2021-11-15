"""
Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do 
aluno e o segundo representando a sua altura em centímetros. Encontre o aluno mais alto e o mais 
baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.
"""

altura_maior = 0
altura_menor = 0
cod_altura_menor = 0
cod_altura_maior = 0
c = 0

for n in range(10):
    cod = int(input(f"Digite o código do {n+1}º aluno: "))
    altura = float(input(f"Digite a altura do {n+1}º aluno (cm): "))
    while c < 1:
        altura_menor = altura
        cod_altura_menor = cod
        c += 1
# Definição de altura maior
    if altura > altura_maior:
        altura_maior = altura
        cod_altura_maior = cod
# Definição de altura menor
    if altura < altura_menor:
        altura_menor = altura
        cod_altura_menor = cod
    print()

print("De acordo com as medidas temos: ")

print (f"Aluno mais alto: Código {cod_altura_maior} / Altura: {altura_maior} cm")
print (f"Aluno mais baixo: Código {cod_altura_menor} / Altura: {altura_menor} cm")
