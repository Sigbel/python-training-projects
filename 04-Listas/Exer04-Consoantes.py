"""
Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
"""

consoantes = []
vogais = ['a', 'e', 'i', 'o', 'u']

for n in range(10):
    letra = str(input(f"Digite a {n+1}ª letra: "))
    
    if letra in vogais:
        continue
    else:
        consoantes.append(letra)

print(f"As consoantes digitadas foram:\n{consoantes}")
print(f"Quantidade de consoantes: {len(consoantes)}")
