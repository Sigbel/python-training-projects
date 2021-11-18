"""
Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada.

F
FU
FUL
FULA
FULAN
FULANO
"""

nome = str(input('Digite seu nome: '))

c = 1
for c1 in nome:
    print(nome[0:c])
    c += 1

