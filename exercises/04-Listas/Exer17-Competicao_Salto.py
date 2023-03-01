"""
Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do atleta será 
determinado pela média dos cinco valores restantes. Você deve fazer um programa que receba o nome e as cinco 
distâncias alcançadas pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos. O programa 
deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:

Atleta: Rodrigo Curvêllo
 
Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Resultado final:
Atleta: Rodrigo Curvêllo
Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
Média dos saltos: 5.9 m
"""

nomes = []
saltos = []
salto_temporario = []

c = 0
while True:
# Atribuição de nome e saltos ás respectivas listas.
    print(f" {c+1}º Atleta ".center(70, '-'))
    nome = str(input(f'Digite o nome do {c+1}º atleta (Vazio para finalizar): '))
    if nome == '':
        break
    nomes.append(nome)

    for c1 in range(5):
        salto = float(input(f'Digite o {c1+1}º salto em metros: '))
        salto_temporario.append(salto)
    
    saltos.append(salto_temporario)
    salto_temporario = []

    c += 1

# Imprime saltos todos os saltos do atleta
for c2 in range(c): 
    print()
    print(f'Atleta: {nomes[c2]}\n')

    for c3, valor in enumerate(saltos[c2]):
        print(f'{c3+1}º Salto: {valor} m')


# Demonstra o resultado final de todos os atletas salvos
print()
print("Resultado final: \n")

for c4 in range(c):
    print(f'Atleta: {nomes[c4]}')
    print('Saltos: ', end='')
    for c5 in range(5):
        print(saltos[c4][c5], end='')
        if c5 == 4:
            break
        print(" - ", end="")
    print()
    print(f'Média dos saltos: {sum(saltos[c4])/5:.2f}\n')
