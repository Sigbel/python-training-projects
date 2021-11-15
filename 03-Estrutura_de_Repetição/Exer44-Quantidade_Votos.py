"""
Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. 
Os códigos utilizados são:

1 , 2, 3, 4  - Votos para os respectivos candidatos 
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco

- Faça um programa que calcule e mostre:
    * O total de votos para cada candidato;
    * O total de votos nulos;
    * O total de votos em branco;
    * A percentagem de votos nulos sobre o total de votos;
    * A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos 
    tem-se o valor zero.
"""

c_1 = 0
c_2 = 0
c_3 = 0
c_4 = 0
c_nulo = 0
c_branco = 0

while True:
    print("Tabela de Candidatos:\n\n1 - João\n2 - Maria\n3 - Cadu\n4 - Tiringa\n\n5 - Nulo\n6 - Branco")
    codigo = int(input("Digite o código equivalente ao candidato: "))
    while codigo < 0 or codigo > 6:
        codigo = int(input("Digite um código válido: "))
    if codigo == 1:
        c_1 += 1
    elif codigo == 2:
        c_2 += 1
    elif codigo == 3:
        c_3 += 1
    elif codigo == 4:
        c_4 += 1
    elif codigo == 5:
        c_nulo += 1
    elif codigo == 6:
        c_branco += 1
    elif codigo == 0:
        break
total_votos = c_1 + c_2 + c_3 + c_4 + c_nulo + c_branco

print(f"Total de Votos por Candidato: \n\nJoão - {c_1}\nMaria - {c_2}\nCadu - {c_3}\nTiringa - {c_4}")
print()
print(f"Total de Votos Nulos: {c_nulo}")
print(f"Total de Votos Brancos: {c_branco}")
print(f"Porcentagem de Votos Nulos sobre o total: {(c_nulo*100)/total_votos:.2f}")
print(f"Porcentagem de Votos Brancos sobre o total: {(c_branco*100)/total_votos:.2f}")
