"""
Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma
pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas 
eleições.
"""

print('-'*30)
def voto(ano_nasci):
    from datetime import date
    ano = date.today().year
    print(f'Com {ano - ano_nasci} anos: ', end='')
    if (ano - ano_nasci) < 16:
        return 'VOTO NEGADO.'
    elif 16 <= (ano - ano_nasci) < 65:
        return'VOTO OBRIGATÓRIO.'
    else:
        return 'VOTO OPCIONAL.'


ano = int(input('Em que ano você nasceu? '))
print(voto(ano))
