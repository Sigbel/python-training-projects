"""
Exercício 14 - Quadrado Mágico

Quadrado mágico. Um quadrado mágico é aquele dividido em linhas e colunas, com um número em cada posição e no qual 
a soma das linhas, colunas e diagonais é a mesma. Por exemplo, veja um quadrado mágico de lado 3, com números de 1 
a 9:

Ex:
8  3  4 
1  5  9
6  7  2

Elabore uma função que identifica e mostra na tela todos os quadrados mágicos com as características acima. Dica: 
produza todas as combinações possíveis e verifique a soma quando completar cada quadrado. Usar um vetor de 1 a 9 
parece ser mais simples que usar uma matriz 3x3.
"""

def teste(arg):
    from itertools import permutations
    
    for c1 in permutations(arg, 9):
        if sum(c1[0:3]) == sum(c1[3:6]) == sum(c1[6:9]):
            if sum(c1[0::3]) == sum(c1[1::3]) == sum(c1[2::3]):
                if sum(c1[0:9:4]) == sum(c1[2:7:2]):
                    print (f'{c1} possível combinação')
    return

# Programa Principal
vetor = [1,2,3,4,5,6,7,8,9]
teste(vetor) 
