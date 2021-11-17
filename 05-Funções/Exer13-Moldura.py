"""
Desenha moldura. Construa uma função que desenhe um retângulo usando os caracteres ‘+’ , ‘−’ e ‘| ‘. Esta função 
deve receber dois parâmetros, linhas e colunas, sendo que o valor por omissão é o valor mínimo igual a 1 e o valor 
máximo é 20. Se valores fora da faixa forem informados, eles devem ser modificados para valores dentro da faixa de 
forma elegante.
"""
def retangulo(linha, coluna):
    for n in range(linha):
        if n == 0 or n == linha-1:
            print('+', '-'*(coluna-2), '+')
        else:
            print('|', ' '*(coluna-2), '|')

   
# Programa Principal
while True:
    line = int(input('Linhas (min 2): '))
    if line == 0:
        break
    while line < 2 or line > 20:
        line = int(input('Verificar o mínimo e máximo de linhas (min - 2 / max - 20): '))
    collum = int(input('Coluna (min 2): '))
    while collum < 2 or collum > 20:
        collum = int(input('Verificar o mínimo e máximo de colunas (min - 2 / max - 20): '))
    retangulo(line, collum)    
