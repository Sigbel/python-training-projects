"""
Exercício 5 - Alteração da População

Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento
iniciais. Valide a entrada e permita repetir a operação.
"""

popu_A = input("Digite a quantidade inicial da população A: ")

#  Valida População de A:
if popu_A.isnumeric():
    popu_A = float(popu_A)
else:
    while type(popu_A) != float:
        popu_A = input("Digite um valor numérico!\nTente novamente: ")
        if popu_A.isnumeric():
            popu_A = float(popu_A)
            continue

# Valida População de B:
popu_B = input("Digite a quantidade inicial da população B: ")

if popu_B.isnumeric():
    popu_B = float(popu_B)
else:
    while type(popu_B) != float:
        popu_B = input("Digite um valor numérico!\nTente novamente: ")
        if popu_B.isnumeric():
            popu_B = float(popu_B)
            continue

contador_anos = 1
taxa_crescimento_A = input("Digite a taxa de crescimento de A em porcentagem (%) (deve ser maior que de B): ")

if taxa_crescimento_A.isnumeric():
    taxa_crescimento_A = float(taxa_crescimento_A)
    while taxa_crescimento_A <= 0:
        taxa_crescimento_A = input("Taxa de crescimento deve ser maior que 0:")
        if taxa_crescimento_A.isnumeric():
            taxa_crescimento_A = float(taxa_crescimento_A)
            continue
else:
    while type(taxa_crescimento_A) != float:
        taxa_crescimento_A = input("Digite um valor numérico.\nTente novamente: ")
        if taxa_crescimento_A.isnumeric():
            taxa_crescimento_A = float(taxa_crescimento_A)
            while taxa_crescimento_A <= 0:
                taxa_crescimento_A = input("Taxa de crescimento deve ser maior que 0:")
                if taxa_crescimento_A.isnumeric():
                    taxa_crescimento_A = float(taxa_crescimento_A)
                    continue
            continue

taxa_crescimento_B = input("Digite a taxa de crescimento de B em porcentagem (%) (deve ser menor que de A): ")

if taxa_crescimento_B.isnumeric():
    taxa_crescimento_B = float(taxa_crescimento_B)
    while taxa_crescimento_B <= 0:
        taxa_crescimento_B = input("Taxa de crescimento deve ser maior que 0:")
        if taxa_crescimento_B.isnumeric():
            taxa_crescimento_B = float(taxa_crescimento_B)
            continue
else:
    while type(taxa_crescimento_B) != float:
        taxa_crescimento_B = input("Digite um valor numérico.\nTente novamente: ")
        print(type(taxa_crescimento_B))
        if taxa_crescimento_B.isnumeric():
            taxa_crescimento_B = float(taxa_crescimento_B)
            print(type(taxa_crescimento_B))
            while taxa_crescimento_B <= 0:
                taxa_crescimento_B = input("Taxa de crescimento deve ser maior que 0:")
                if taxa_crescimento_B.isnumeric():
                    taxa_crescimento_B = float(taxa_crescimento_B)
                    continue
            continue

if taxa_crescimento_B > taxa_crescimento_A:
    print("Por favor, a taxa B deve ser menor que A.")

while popu_A < popu_B:
    aumento_A = popu_A * (taxa_crescimento_A/100)
    aumento_B = popu_B * (taxa_crescimento_B/100)
    popu_A = popu_A + aumento_A
    popu_B = popu_B + aumento_B
    contador_anos += 1

print(f"A população da cidade A chegará a mesma quantidade da cidade B em: {contador_anos} anos")
