"""
Exercício 5 - Nome na Vertical (Escada Invertida)

Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja invertida.

FULANO
FULAN
FULA
FUL
FU
F
"""

nome = str(input('Digite seu nome: '))

c = -1
for c1 in nome:
    if c == -1:
        print(nome)
    print(nome[0:c])
    if c1 == nome[-2]:
        break
    c -= 1

