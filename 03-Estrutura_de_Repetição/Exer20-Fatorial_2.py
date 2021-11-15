"""
Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes 
e limitando o fatorial a números inteiros positivos e menores que 16.
"""

while True:
    termo_1 = int(input("Digite um número para calcular o fatorial: "))
    while termo_1 < 0 or termo_1 > 16:
        termo_1 = int(input("Por favor, digite um número inteiro positivo e menor que 16.\nTente novamente: "))
    termo_1_temp = termo_1
    fatorial = 0

    for n in range(termo_1-1):
        termo_seg = termo_1 - (n+1)
        fatorial = termo_1_temp * termo_seg
        termo_1_temp = fatorial

    print(fatorial)
    continua = input("Deseja continuar? [s]im ou [n]ão: ").upper()
    while (continua != "N") and (continua != "S"): 
        continua = input("Digite um parâmetro válido.\nTente novamente: ").upper()
    if continua == "N":
        break
    elif continua == "S":
        continue

print("Fim do Programa.")
