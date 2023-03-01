"""
Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados 
quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:

- Mostre a quantidade de valores que foram lidos;
- Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
- Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
- Calcule e mostre a soma dos valores;
- Calcule e mostre a média dos valores;
- Calcule e mostre a quantidade de valores acima da média calculada;
- Calcule e mostre a quantidade de valores abaixo de sete;
- Encerre o programa com uma mensagem;
"""

valores = []
valores_maiores_media = []
valores_abaixo_7 = []
soma = 0

c = 0
while True:
    num = float(input(f"Digite o {c+1}º valor (-1 para sair): "))
    if num == -1:
        break
    valores.append(num)
    soma += num
    c += 1

media = soma/c

for c1 in valores:
    if c1 > media:
        valores_maiores_media.append(c1)
    if c1 < 7:
        valores_abaixo_7.append(c1)

print()
print(f"Quantidade de valores: {len(valores)}\n")
print(f"Valores na ordem que foram informados:\n{valores}\n")
print(f"Valores na ordem inversa:\n{valores[::-1]}\n")
print(f"A soma dos valores é {soma}\n")
print(f"A média dos valores é {soma/c}\n")
print(f"Quantidade de valores acima da média: {len(valores_maiores_media)}\n")
print(f"Quantidade de valores abaixo de 7: {len(valores_abaixo_7)}\n")

print("Fim do Programa!")
