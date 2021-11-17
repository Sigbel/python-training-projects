"""
Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digita o comando e o manual vai
aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará.

OBS: use cores.
"""
from time import sleep


def func(parameter):
    print('\033[1;97;104m~'*(34+len(parameter)))
    print(f'Acessando o manual do comando "{parameter}"'.center(34+len(parameter)))
    print('~'*(34+len(parameter)))
    print('\033[m', end='')
    
    sleep(1.5)
    print('\033[1;30;107m', end='')
    help(parameter)
    return


while True:
    print('\033[1;97;102m~'*27)
    print('SISTEMA DE AJUDA PyHELP'.center(27))
    print('\033[1;97;102m~'*27)
    print('\033[m', end='')

    param = str(input('Função ou Biblioteca > '))
    if param == 'fim':
        break

    func(param)

    sleep(1.5)

print('\033[1;97;41m~'*27)
print('ATÉ LOGO'.center(27))
print('~'*27)
print('\033[m')
   
