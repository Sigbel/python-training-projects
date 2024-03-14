"""
Exercício 12 - Idade e Altura (2)

Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 
anos possuem altura inferior à média de altura desses alunos.
"""

idades_13 = []
alturas_13 = []
soma_altura = 0

for c1 in range(30):
    print(f"Aluno {c1+1}")
    idade = int(input(f"Digite a idade do {c1+1}º aluno: "))
    altura = float(input(f"Digite a altura do {c1+1}º aluno: "))

    if idade > 13:
        idades_13.append(idade)
        alturas_13.append(altura)

    soma_altura += altura

media_altura = soma_altura/30

contador_central = 0

for c2 in range(len(idades_13)):
    if alturas_13[c2] < media_altura:
        contador_central += 1

print(f"A quantidade de alunos com mais de 13 anos e com altura inferior a média é: {contador_central}")
