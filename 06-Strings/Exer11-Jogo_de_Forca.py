"""
Jogo de Forca. Desenvolva um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo 
texto e escolherá uma aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado.

Digite uma letra: A
-> Você errou pela 1ª vez. Tente de novo!

Digite uma letra: O
A palavra é: _ _ _ _ O

Digite uma letra: E
A palavra é: _ E _ _ O

Digite uma letra: S
-> Você errou pela 2ª vez. Tente de novo!
"""
from random import randint

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
palavra_indefinida = ['_' for c1 in palavra_chave]
palavra_final = ''.join(palavra_chave)

# Jogo
contador_erros = 0
while True:
    letra = str(input('Digite uma letra: ')).upper()
    if letra == '':
        break
    if letra not in palavra_final:
        contador_erros += 1
        if contador_erros == 6:
            print(f'Você perdeu! A palavra era: {palavra_selecionada}' )
            break
        print(f'-> Você errou pela {contador_erros}ª vez. Tente de novo!')
    else:
        while letra in palavra_chave:
            index = palavra_chave.index(letra)
            palavra_indefinida[index] = letra
            palavra_chave[index] = '*'
        print(f'A palavra é: {" ".join(palavra_indefinida)}')
    
    if ''.join(palavra_indefinida) == palavra_final:
        print(f'Você ganhou, a palavra era {palavra_selecionada}')
        break
    print()
