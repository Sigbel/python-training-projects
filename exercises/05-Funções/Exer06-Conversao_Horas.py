"""
Exercício 6 - Conversão de Horas

Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo, o programa deve 
converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. Deve haver pelo menos duas funções: uma para fazer 
a conversão e uma para a saída. Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M. Assim, 
a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M. Inclua um loop que 
permita que o usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar.
"""

def converte(*args):
    h = args[0]
    m = args[1]

    while h > 24:
        h = int(input('Por favor digite as horas num intervalo de 12 a 24 hrs: '))
    while m < 0 or m > 60:
        m = int(input('Por favor digite os minutos num intervalo de 0 a 60 min: '))
    h = h - 12
    return f'{h}:{m} PM'

def saida(horas, minutos):
    h = horas
    m = minutos

    while h > 24 or h < 0:
        h = int(input('Digite um valor ente 0 e 24: '))
    while m > 60 or m < 0:
        m = int(input('Digite um valor ente 0 e 60: '))
    if h > 12:
            return converte(horas, minutos)
    else: 
        while h < 0:
            h = int(input('Por favor digite as horas num intervalo de 12 a 24 hrs: '))
        while m < 0 or m > 60:
            m = int(input('Por favor digite os minutos num intervalo de 0 a 60 min: '))
        return f'{h}:{m} AM'

while True: 
    horas = str(input('Digite um horário separado por ":" = '))
    while len(horas) != 5:
        horas = str(input('Digite um horário válido separado por ":" = '))

    lista_hora = horas.split(':')

    print(saida(int(lista_hora[0]), int(lista_hora[1])))
    continua = str(input('Deseja continuar? [s]im ou [n]ao: ')).upper()
    while continua != 'S' and continua != 'N':
        continua = str(input('Somente "S" ou "N": ')).upper()
    if continua == 'N':
        break
