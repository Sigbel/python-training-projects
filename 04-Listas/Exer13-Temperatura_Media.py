"""
Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule
a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram 
(mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
"""

temperatura_media = []
soma = 0

for c1 in range(12):
    temperatura = float(input(f"Digite a temperatura média no mês {c1+1}: "))
    temperatura_media.append(temperatura)
    soma += temperatura

media = soma/12

meses_maior_media = []

for c2 in range(len(temperatura_media)):
    
    if temperatura_media[c2] > media:
        meses_maior_media.append(c2+1)

print()
print(f"Meses com temperatura maior que a média anual ({media:.2f}º): ")
for c3 in meses_maior_media:
    if c3 == 1:
        print("- Janeiro") 
    elif c3 == 2:
        print("- Fevereiro") 
    elif c3 == 3:
        print("- Março") 
    elif c3 == 4:
        print("- Abril") 
    elif c3 == 5:
        print("- Maio") 
    elif c3 == 6:
        print("- Junho") 
    elif c3 == 7:
        print("- Julho") 
    elif c3 == 8:
        print("- Agosto") 
    elif c3 == 9:
        print("- Setembro") 
    elif c3 == 10:
        print("- Outubro") 
    elif c3 == 11:
        print("- Novembro") 
    elif c3 == 12:
        print("- Dezembro") 
