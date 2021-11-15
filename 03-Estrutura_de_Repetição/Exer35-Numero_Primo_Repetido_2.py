"""
Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números 
primos existentes entre 1 e um número inteiro informado pelo usuário.
"""

n_termos = int(input("Digite o último número do intervalo: "))
primo = True
c = 2
divisoes = 0

print()
print("Os números primos nesse intervalo são: ")
while c < n_termos:
    for n in range(c-2):
        teste = c % (n+2)
        divisoes += 1
        if teste == 0:
            primo = False

    if primo:
        print(f"{c}", end=" ")
    primo = True
    c += 1

