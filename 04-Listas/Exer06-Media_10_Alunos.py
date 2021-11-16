"""
Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, 
imprima o número de alunos com média maior ou igual a 7.0.
"""

medias = []
contador = 0

for c1 in range(10):
    print(f"Aluno {c1+1}")
    soma = 0
    for c2 in range(4):
        nota = float(input(f"Digite a {c2+1}ª nota: "))
        soma += nota
    media = soma/4
    medias.append(media)

for c3 in medias:
    if c3 >= 7:
        contador += 1

print(f"O número de alunos com média maior que 7 é: {contador}")
