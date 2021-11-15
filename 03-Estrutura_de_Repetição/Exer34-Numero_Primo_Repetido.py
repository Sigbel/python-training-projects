"""
Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. 
Um número primo é aquele que é divisível apenas por um e por ele mesmo. Faça um programa que peça 
um número inteiro e determine se ele é ou não um número primo.
"""

num_teste = int(input("Digite o número a ser testado: "))
ele_mesmo = True

for n in range(num_teste-2):
    teste = num_teste % (n+2)
    if teste == 0:
        print("Número não é primo!")
        ele_mesmo = False
        break

if ele_mesmo:
    print("É primo!")
