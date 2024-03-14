"""
Exercício 5 - Aprovação do Aluno

Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
- A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
- A mensagem "Reprovado", se a média for menor do que sete;
- A mensagem "Aprovado com Distinção", se a média for igual a dez.
"""

nota_01 = float(input("Digite a 1ª nota: "))
nota_02 = float(input("Digite a 2ª nota: "))
media = (nota_01+nota_02)/2

if 7 <= media < 10:
    print("Aprovado!")
elif media < 7:
    print("Reprovado!")
elif media == 10:
    print("Aprovado com Distinção!")