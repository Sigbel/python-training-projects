"""
Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de 
turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.
"""

qtde_turmas = int(input("Digite a quantidade de turmas: "))
soma = 0

for n in range(qtde_turmas):
    num_alunos =  int(input(f"Digite a quantidade de alunos na {n+1}ª turma: "))
    while num_alunos > 40:
        num_alunos = int(input(f"A turma só pode ter até 40 alunos.\nTente novamente: "))
    soma = num_alunos + soma

print(f"A média de alunos por sala é de {soma//qtde_turmas}")
