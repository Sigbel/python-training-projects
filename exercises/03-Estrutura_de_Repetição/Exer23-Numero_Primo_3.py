"""
Exercício 23 - Número Primo (3)

Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo 
usuário. O programa deverá mostrar também o número de divisões que ele executou para encontrar os 
números primos. Serão avaliados o funcionamento, o estilo e o número de testes (divisões) 
executados.
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

print()
print(f"Numero de diviões executadas até o fim do programa: {divisoes}")
