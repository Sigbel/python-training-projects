"""
Exercício 46 - Salto a Distância

Em uma competição de salto em distância cada atleta tem direito a cinco saltos. No final da série 
de saltos de cada atleta, o melhor e o pior resultados são eliminados. O seu resultado fica sendo 
a média dos três valores restantes. Você deve fazer um programa que receba o nome e as cinco 
distâncias alcançadas pelo atleta em seus saltos e depois informe a média dos saltos conforme a 
descrição acima informada (retirar o melhor e o pior salto e depois calcular a média). Faça uso de 
uma lista para armazenar os saltos. Os saltos são informados na ordem da execução, portanto não 
são ordenados. O programa deve ser encerrado quando não for informado o nome do atleta. A saída 
do programa deve ser conforme o exemplo abaixo:

Atleta: Rodrigo Curvêllo

Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Melhor salto:  6.5 m
Pior salto: 5.3 m
Média dos demais saltos: 5.9 m

Resultado final:
Rodrigo Curvêllo: 5.9 m
"""

saltos = []
atletas = []
medias_saltos = []
nome = ""
c = 0
melhor_salto = 0
pior_salto = 0

while True:
    nome = str(input("Digite o nome do Atleta: "))
    if nome == "":
        print()
        print("Resultado Final: ")
        c_lista = 0
        
        for qtde in atletas:
            print(f"{qtde}: {medias_saltos[c_lista]:.2f} m")
            c_lista += 1
        break
    
    atletas.append(nome)
    
    for n in range(5):
        valor = float(input(f"{n+1}º Salto: "))
        saltos.append(valor)
        while c < 1:
            pior_salto = saltos[n]
            c += 1
        if saltos[n] > melhor_salto:
            melhor_salto = saltos[n]
        if saltos[n] < pior_salto:
            pior_salto = saltos[n]
    
    media = (sum(saltos)-melhor_salto-pior_salto)/3
    medias_saltos.append(media)
    
    print()
    print(f"Atleta: {nome}\n")
    
    for p in range(5):
        print(f"{p+1}º Salto: {saltos[p]} m")
    
    print()
    print(f"Melhor Salto: {melhor_salto} m\nPior Salto: {pior_salto} m")
    print(f"Média dos demais Saltos: {media:.2f} m")
    saltos = []
    melhor_salto = 0
    pior_salto = 0
    c = 0
