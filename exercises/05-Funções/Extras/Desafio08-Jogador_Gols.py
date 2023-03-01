"""
    Faça um programa que tenha uma função ficha(), que receba dois parâmetros opcinais: o nome de um jogador e
quantos gols ele marcou.
    O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado
corretamente.
"""

def ficha(jogador, gols):
    print(f'O jogador {jogador} fez {gols} gol(s) no campeonato.')

jogador = str(input('Nome do Jogador: '))
if jogador == '':
    jogador = '<desconhecido>'
gols = input('Número do Gols: ')
if gols == '':
    gols = 0
ficha(jogador,gols)
