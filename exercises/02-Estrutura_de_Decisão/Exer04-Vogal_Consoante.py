"""
Exercício 4 - Vogal e Consoante

Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

"""

letra = str(input("Digite uma letra: "))

if len(letra) == 1:
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        print("A letra é uma vogal.")
    else:
        print("A letra é uma consoante.")
else:
    print("Digite apenas uma letra!")