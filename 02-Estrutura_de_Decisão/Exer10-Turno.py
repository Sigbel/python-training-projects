"""
Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou
"Boa Noite!" ou "Valor Inválido!", conforme o caso.
"""

letra = str(input("Digite a letra correspondente ao genêro (M), (V) ou (N): ")).upper()

if letra == "M":
    print("Bom Dia!")
elif letra == "V":
    print("Boa Tarde!")
elif letra == "N":
    print("Boa Noite!")
else:
    print("Valor Inválido!")