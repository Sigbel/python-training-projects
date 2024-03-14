"""
Exercício 22 - Número Primo (2)

Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por 
quais número ele é divisível.
"""

num_teste = int(input("Digite o número a ser testado: "))
primo = True
c = 0

for n in range(num_teste-2):
    teste = num_teste % (n+2)
    if teste == 0:
        while c < 1:
            print("O numero é não primo, sendo divisível por: ",end="")
            c += 1
        print(f"{n+2}", end=" ")
        primo = False

if primo:
    print("É primo!")
