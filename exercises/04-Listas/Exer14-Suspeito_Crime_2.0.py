"""
Exercício 14 - Suspeito do Crime (2)

Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
- "Telefonou para a vítima?"
- "Esteve no local do crime?"
- "Mora perto da vítima?"
- "Devia para a vítima?"
- "Já trabalhou com a vítima?" 

O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder 
positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como 
"Assassino". Caso contrário, ele será classificado como "Inocente".
"""

perguntas = ["Telefonou para a vítima?", "Esteve no local do crime?", "Mora perto da vítima?",
"Devia para a vitima?", "Já trabalhou com a vítima?"]
respostas = []

for c1 in perguntas:
    resposta = str(input(f"{c1} [s]im ou [n]ão: ")).upper()
    while resposta != "S" and resposta != "N":
        resposta = str(input("Digite um caractere válido: ")).upper()
    respostas.append(resposta)

c_sim = 0
for c2 in respostas:
    if c2 == "S":
        c_sim += 1

print()

if c_sim == 2:
    print("Essa pessoa é suspeita.")
elif c_sim == 3 or c_sim == 4:
    print("Essa pessoa é Cúmplice.")
elif c_sim == 5:
    print("Essa pessoa é a ASSASSINA!")
else:
    print("Essa pessoa é inocente.")
