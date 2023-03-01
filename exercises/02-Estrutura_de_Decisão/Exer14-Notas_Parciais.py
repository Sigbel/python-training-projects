"""
Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece
à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E

  O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.
"""

nota_01 = float(input("Digite a 1ª nota: "))
nota_02 = float(input("Digite a 2ª nota: "))
media = (nota_01 + nota_02)/2
conceito = 0
status = 0

if 0 < media <= 4:
    conceito = "E"
elif 4 < media <= 6:
    conceito = "D"
elif 6 < media <= 7.5:
    conceito = "C"
elif 7.5 < media < 9:
    conceito = "B"
else:
    conceito = "A"

if conceito == "E" or conceito == "D":
    status = "REPROVADO"
else:
    status = "APROVADO"
print()
print(f"A Notas foram: {nota_01} e {nota_02}\nA média foi: {media}\nO conceito correspondente a média é: {conceito}\nStatus: {status} ")