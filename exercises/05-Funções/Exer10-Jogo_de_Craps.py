"""
Jogo de Craps. Faça um programa de implemente um jogo de Craps. O jogador lança um par de dados, obtendo um valor 
entre 2 e 12. Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou. Se você tirar 2, 3 ou 12 na 
primeira jogada, isto é chamado de "craps" e você perdeu. Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,
este é seu "Ponto". Seu objetivo agora é continuar jogando os dados até tirar este número novamente. Você perde, 
no entanto, se tirar um 7 antes de tirar este Ponto novamente.
"""
def dados():
    from random import randint
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)
    soma = dado1 + dado2
    return soma

def craps(inicia):
    craps = [2, 3, 12]
    normal = [7, 11]
    valor = dados()
    if valor in normal:
        return f'Você rolou {valor}, você é um NORMAL. Você Ganhou!!'
    if valor in craps:
        return f'Você rolou {valor}, CRAPS! Você Perdeu!!'
    else:
        valor_temp = 0
        print(f'Você rolou {valor} e fez um "Ponto"')
        while True:
            continua = str(input('Continue jogando. [s] para jogar: ')).upper()
            while continua != 'S':
                continua = str(input('Favor digitar apenas [s] para jogar: ')).upper()
            valor_temp = dados()
            if valor_temp == valor:
                return f'Você rolou {valor_temp}, fez outro ponto e ganhou!!'
            print(f'Você rolou {valor_temp}')
            if valor_temp == 7:
                return 'Você tirou 7 antes do ponto e perdeu :('


# Programa Principal    
inicio = str(input('Gostaria de iniciar? [s]im ou [n]ão: ')).upper()
while inicio != 'S' and inicio != 'N':
    inicio = str(input('Por favor, digite somente "s" ou "n": '))
print(craps(inicio))
