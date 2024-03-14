"""
Exercício 12 - Valida e Corrige Número do Telefone

Valida e corrige número de telefone. Faça um programa que leia um número de telefone, e corrija o número 
no caso deste conter somente 7 dígitos, acrescentando o '3' na frente. O usuário pode informar o número 
com ou sem o traço separador.

Valida e corrige número de telefone
Telefone: 461-0133
Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.
Telefone corrigido sem formatação: 34610133
Telefone corrigido com formatação: 3461-0133
"""
print('Valida e corrige número de telefone')

telefone = input('Telefone: ')
lista = [c1 for c1 in telefone.replace('-', '')]

while (len(lista) > 8 or len(lista) < 7) or not ''.join(lista).isnumeric():
    telefone = input('Telefone Inválido. Tente novamente:  ')
    lista = [c1 for c1 in telefone.replace('-', '')]

if len(lista) == 7:
    print('Telefone possui 7 digitos. Vou acrescentar o digito três na frente.')
    lista.insert(0, '3')

print(f'Telefone corrigido sem formatação: {"".join(lista)}')
formata = ''.join(lista)
lista_1 = [formata[0:4]]
lista_2 = [formata[4:9]]

print(f'Telefone corrigido com formatação: {"-".join(lista_1+lista_2)}')
