"""
Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. 
Imprima a idade e a altura na ordem inversa a ordem lida.
"""

idades = []
alturas = []

for n in range(5):
    print(f"Pessoa {n+1}")
    idade = int(input(f"Digite a {n+1}ª idade: "))
    idades.append(idade)
    altura = float(input(f"Digite a {n+1}ª altura: "))
    alturas.append(altura)
    
print(f"Idades na ordem inversa: {idades[::-1]}")
print(f"Alturas na ordem inversa: {alturas[::-1]}")
