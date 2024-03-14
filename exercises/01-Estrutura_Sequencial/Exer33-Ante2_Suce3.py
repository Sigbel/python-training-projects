"""
Exercício 33 - Anterior e Sucessor (2)

Faça um programa retorne a soma do sucessor do triplo e antecessor do dobro de um número fornecido.
"""

num = int(input("Digite um número: "))

suc = (num*3)+1
ant = (num*2)-1

print(f"A soma dos sucessor do triplo com o antecessor do dobro é: {suc+ant}")