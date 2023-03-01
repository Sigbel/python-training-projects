"""
Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
    a. A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
    b. A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
    c. A mensagem "Aprovado com Distinção", se a média for igual a 10.
"""

nota_01 = float(input("Digite a 1ª nota: "))
nota_02 = float(input("Digite a 2ª nota: "))
nota_03 = float(input("Digite a 3ª nota: "))
media = (nota_01+nota_02+nota_03)/3

if 7 <= media < 10:
    print(f"Sua média foi: {media:.2f}\nAprovado!")
elif media < 7:
    print(f"Sua média foi: {media:.2f}\nReprovado!")
elif media == 10:
    print(f"Sua média foi: {media:.2f}\nAprovado com Distinção!")
