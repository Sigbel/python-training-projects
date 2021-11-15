"""
Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa 
deve perguntar ao aluno a resposta de cada questão e ao final comparar com o gabarito da prova e 
assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa). Após cada aluno
utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema. Após todos os 
alunos terem respondido informar:

    - Maior e Menor Acerto;
    - Total de Alunos que utilizaram o sistema;
    - A Média das Notas da Turma.

Gabarito da Prova:

01 - A
02 - B
03 - C
04 - D
05 - E
06 - E
07 - D
08 - C
09 - B
10 - A

Após concluir isto você poderia incrementar o programa permitindo que o professor digite o gabarito 
da prova antes dos alunos usarem o programa.
"""

print("Digite o gabarito da prova: \n")

gabarito1 = str(input("Questão 1: ")).upper()
gabarito2 = str(input("Questão 2: ")).upper()
gabarito3 = str(input("Questão 3: ")).upper()
gabarito4 = str(input("Questão 4: ")).upper()
gabarito5 = str(input("Questão 5: ")).upper()
gabarito6 = str(input("Questão 6: ")).upper()
gabarito7 = str(input("Questão 7: ")).upper()
gabarito8 = str(input("Questão 8: ")).upper()
gabarito9 = str(input("Questão 9: ")).upper()
gabarito10 = str(input("Questão 10: ")).upper()
print()
soma_acertos = 0
maior_acerto = 0
menor_acerto = 0
c_alunos = 0
c = 0
acerto = 0

while True:
    for n in range(10):
        print(f"Aluno {n+1}")
        respostas = str(input(f"{n+1} - ")).upper()
        if n == 0 and respostas == gabarito1:
            acerto += 1
        elif n == 1 and respostas == gabarito2:
            acerto += 1
        elif n == 2 and respostas == gabarito3:
            acerto += 1
        elif n == 3 and respostas == gabarito4:
            acerto += 1
        elif n == 4 and respostas == gabarito5:
            acerto += 1
        elif n == 5 and respostas == gabarito6:
            acerto += 1
        elif n == 6 and respostas == gabarito7:
            acerto += 1
        elif n == 7 and respostas == gabarito8:
            acerto += 1
        elif n == 8 and respostas == gabarito9:
            acerto += 1
        elif n == 9 and respostas == gabarito10:
            acerto += 1
    while c < 1:
        menor_acerto = acerto
        c +=1
    if acerto > maior_acerto:
        maior_acerto = acerto
    if acerto < menor_acerto:
        menor_acerto = acerto
    soma_acertos = soma_acertos + acerto
    c_alunos += 1
    continua = str(input("Continua? [S]im ou [N]ão: ")).upper()
    while continua != "S" and continua != "N":
        continua = str(input("Digite um parâmetro válido: ")).upper()
    if continua == "N":
        break
    else:
        acerto = 0
        continue

print(f"O maior número de acertos foi: {maior_acerto}")
print(f"O menor número de acertos foi: {menor_acerto}")
print()
print(f"Total de alunos que utilizaram o sistema: {c_alunos}")
print()
print(f"A média das notas da turma: {soma_acertos/c_alunos:.2f}")
