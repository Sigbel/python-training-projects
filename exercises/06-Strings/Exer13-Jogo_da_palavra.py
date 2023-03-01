"""
Jogo da palavra embaralhada. Desenvolva um jogo em que o usuário tenha que adivinhar uma palavra que será 
mostrada com as letras embaralhadas. O programa terá uma lista de palavras lidas de um arquivo texto e 
escolherá uma aleatoriamente. O jogador terá seis tentativas para adivinhar a palavra. Ao final a palavra 
deve ser mostrada na tela, informando se o usuário ganhou ou perdeu o jogo.
"""
from random import randint, shuffle

file = open('palavras.txt', 'r')
# Acha quantidade de linhas no arquivo
file.seek(0, 0)
c = 0
for linha in file:
    c += 1
# Seleciona uma linha aleatória dentro do range definido
file.seek(0, 0)
randomico = randint(1, c)
content = file.readlines()
palavra_selecionada = content[randomico-1].upper()

file.close()

palavra_chave = [c1 for c1 in palavra_selecionada]
palavra_chave.remove('\n')
palavra_final = ''.join(palavra_chave)

# Jogo
print('Adivinhe a Palavra:')
shuffle(palavra_chave)
print(palavra_chave)
print()

c = 6
while True:
    palavra = str(input('Qual é a palavra: ')).upper()
    if palavra == palavra_final:
        print(f'Parabéns você acertou! Palavra: {palavra_final}')
        break
    else:
        if c == 1:
            print('Você perdeu!')
            break
        c -= 1
        print(f'Você errou. Tentativas restantes: {c}')