"""
Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a 
média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é 
jovem, adulta ou idosa, conforme a média calculada.
"""

numero_pessoas = int(input("Digite a quantidade de pessoas: "))
soma = 0

for n in range(numero_pessoas):
    idade = int(input(f"Digite a idade da {n+1}ª pessoa: "))
    soma = idade + soma

media = soma/numero_pessoas

print()
if 0 < media <= 25:
    print("A turma é proveniente de jovens!")
elif 25 < media < 60:
    print("A turma é proveniente de adultos!")
else:
    print("A turma é proveniente de idosos!")
