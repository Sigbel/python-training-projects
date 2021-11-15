"""
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. 
Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:

Fatorial de: 5
5! =  5 . 4 . 3 . 2 . 1 = 120
"""

termo_1 = int(input("Digite um número para calcular o fatorial: "))
termo_1_temp = termo_1
fatorial = 0

print(f"Fatorial de: {termo_1}\n{termo_1}! = {termo_1}", end=" ")
for n in range(termo_1-1):
    print(f". {termo_1-(n+1)}",end=" ")
    termo_seg = termo_1 - (n+1)
    fatorial = termo_1_temp * termo_seg
    termo_1_temp = fatorial
    

print(f"= {fatorial}")
