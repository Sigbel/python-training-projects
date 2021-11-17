"""
Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número
a calcular e o outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na
tela o processo de cálculo do fatorial.
"""

def fatorial(num, show=False):
    """
    Calcula o fatorial do número informado
    - param n = O número calculado.
    - param show = (opcional) Mostrar ou não a conta.
    - return = O valor do fatorial de um número n.
    """
    f = 1
    for n in range(num, 0, -1):
        f *= n  
        if show:
            print(f'{n}', end='')
            if n != 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
    print(f)

fatorial(4, show=True)
