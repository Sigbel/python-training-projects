"""
Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor e a pior nota 
são eliminadas. A sua nota fica sendo a média dos votos restantes. Você deve fazer um programa que 
receba o nome do ginasta e as notas dos sete jurados alcançadas pelo atleta em sua apresentação e 
depois informe a sua média, conforme a descrição acima informada (retirar o melhor e o pior salto 
e depois calcular a média com as notas restantes). As notas não são informados ordenadas. Um 
exemplo de saída do programa deve ser conforme o exemplo abaixo:

Atleta: Aparecido Parente
Nota: 9.9
Nota: 7.5
Nota: 9.5
Nota: 8.5
Nota: 9.0
Nota: 8.5
Nota: 9.7

Resultado final:
Atleta: Aparecido Parente
Melhor nota: 9.9
Pior nota: 7.5
Média: 9,04
"""

saltos = []
atletas = []
medias_notas = []
c = 0
melhor_nota_lista = []
melhor_nota = 0
pior_nota_lista = []
pior_nota = 0

while True:
    nome = str(input("Digite o nome do Atleta: "))
    if nome == "":
        print()
        print("Resultado Final: ")
        c_lista = 0
        for qtde in atletas:
            print(f"Atleta: {qtde}")
            print(f"Melhor Nota: {melhor_nota_lista[c_lista]}")
            print(f"Pior Nota: {pior_nota_lista[c_lista]}")
            print(f"Média: {medias_notas[c_lista]:.2f}")
            print("-"*50)
            c_lista += 1
        break
    
    atletas.append(nome)
    
    for n in range(7):
        valor = float(input(f"Nota: "))
        saltos.append(valor)
        while c < 1:
            pior_nota = saltos[n]
            c += 1
        if saltos[n] > melhor_nota:
            melhor_nota = saltos[n]
        if saltos[n] < pior_nota:
            pior_nota = saltos[n]

    melhor_nota_lista.append(melhor_nota)
    pior_nota_lista.append(pior_nota)
    media = (sum(saltos)-melhor_nota-pior_nota)/5
    medias_notas.append(media)
    
    print()
    print(f"Atleta: {nome}\n")
    
    for p in range(7):
        print(f"Nota: {saltos[p]}")
    
    print()
    
    print(f"Melhor nota: {melhor_nota}\nPior nota: {pior_nota}")
    print(f"Média: {media:.2f}")
    saltos = []
    melhor_nota = 0
    pior_nota = 0
    c = 0
