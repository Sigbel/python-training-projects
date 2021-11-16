"""
Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor. 
Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor de contadores(1-6) e uma função para 
gerar numeros aleatórios, simulando os lançamentos dos dados.
"""

from random import randrange

contador_faces = [0,0,0,0,0,0]

for c1 in range(100):
    num = randrange(1, 7)
    contador_faces[num-1] += 1

for c2 in range(6):
    print(f'{c2+1} = {contador_faces[c2]} vezes')
