"""
Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de 
crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 
1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do 
país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
"""

popu_A = 80000
popu_B = 200000
contador_anos = 1

while popu_A < popu_B:
    aumento_A = popu_A * 0.03
    aumento_B = popu_B * 0.015
    popu_A = popu_A + aumento_A
    popu_B = popu_B + aumento_B
    contador_anos += 1

print(f"A população da cidade A chegará a mesma quantidade da cidade B em: {contador_anos} anos")
