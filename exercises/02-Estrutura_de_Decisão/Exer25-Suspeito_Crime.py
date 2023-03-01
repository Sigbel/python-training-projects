"""
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?"

O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder
positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
Caso contrário, ele será classificado como "Inocente".
"""

pergunta01 = str(input("Telefonou para a vitima? (S) ou (N): ")).upper()
pergunta02 = str(input("Esteve no local do crime? (S) ou (N): ")).upper()
pergunta03 = str(input("Mora perto da vitima? (S) ou (N): ")).upper()
pergunta04 = str(input("Devia para a vitima? (S) ou (N): ")).upper()
pergunta05 = str(input("Já Trabalhou com a vitima? (S) ou (N): ")).upper()
contador_sim = 0
pergunta = [pergunta01, pergunta02, pergunta03, pergunta04, pergunta05]
if pergunta01 != "S" and pergunta01 != "N":
    print("Digite uma letra válida!")
elif pergunta02 != "S" and pergunta02 != "N":
    print("Digite uma letra válida!")
elif pergunta03 != "S" and pergunta03 != "N":
    print("Digite uma letra válida!")
elif pergunta04 != "S" and pergunta04 != "N":
    print("Digite uma letra válida!")
elif pergunta05 != "S" and pergunta05 != "N":
    print("Digite uma letra válida!")
else:
    if pergunta01 == "S":
        contador_sim += 1
    if pergunta02 == "S":
        contador_sim += 1
    if pergunta03 == "S":
        contador_sim += 1
    if pergunta04 == "S":
        contador_sim += 1
    if pergunta05 == "S":
        contador_sim += 1
    if contador_sim == 2:
        print("Essa pessoa é suspeita!")
    elif contador_sim == 3 or contador_sim == 4:
        print("Essa pessoa é cumplice!")
    elif contador_sim == 5:
        print("Você está diante do assassino!")
    else:
        print("Essa pessoa é inocente!")
