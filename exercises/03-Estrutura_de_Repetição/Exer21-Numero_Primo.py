"""
Exercício 21 - Número Primo

Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número 
primo é aquele que é divisível somente por ele mesmo e por 1.
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
        
