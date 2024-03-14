"""
Exercício 7 - Conta Espaço de Vogais

Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:

quantos espaços em branco existem na frase.
quantas vezes aparecem as vogais a, e, i, o, u.
"""
string = str(input('Digite uma string: ')).upper()

vogais = ['A', 'E', 'I', 'O', 'U']
contador_vogais = 0

for c1 in vogais:
    contador_vogais += string.count(c1)

print(f'Espaços em branco: {string.count(" ")}')
print(f'Vogais: {contador_vogais}')
