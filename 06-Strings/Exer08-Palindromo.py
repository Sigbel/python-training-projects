"""
Palíndromo. Um palíndromo é uma seqüência de caracteres cuja leitura é idêntica se feita da direita para esquerda ou 
ice−versa. Por exemplo: OSSO e OVO são palíndromos. Em textos mais complexos os espaços e pontuação são ignorados. A 
frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma onde os espaços foram ignorados. Faça um programa que leia 
uma seqüência de caracteres, mostre−a e diga se é um palíndromo ou não.
"""
print('Identificador de Palíndromos\n')

string = str(input('Digite uma string: ')).upper()
string = string.replace(' ', '')
lista_1 = [c1 for c1 in string]

if lista_1 == lista_1[::-1]:
    print('É Palíndromo.')
else:
    print('Não é Palíndromo.')

