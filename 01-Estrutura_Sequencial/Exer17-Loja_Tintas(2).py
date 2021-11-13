"""
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para
cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
- comprar apenas latas de 18 litros;
- comprar apenas galões de 3,6 litros;
- misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
"""

metros_quadrados = float(input("Digite quantos metros quadrados vão ser pintados: "))
quantidade18 = metros_quadrados/(18*6)
quantidade3_6 = metros_quadrados/(3.6*6)
exata18 = round(quantidade18+0.5)  # arredonda para cima o número de latas 18L
exata3_6 = round(quantidade3_6+0.5)  # arredonda para cima o número de latas de 3.6L
metros_temp = metros_quadrados
contador18 = 0
contador3_6 = 0
while metros_temp > 0:
    if metros_temp >= 108:
        while metros_temp >= 108:
            metros_temp = metros_temp - 108
            contador18 += 1
    else:
        while 0 < metros_temp < 108:
            metros_temp = metros_temp - 21.6
            contador3_6 += 1

print(f"A quantidade de latas de 18L vai ser: {exata18} e o valor pago será: R${exata18*80}")
print(f"A quantidade de latas de 3.6L vai ser: {exata3_6} e o valor pago será: R${exata3_6*25}")
print()
print(f"Se misturamos as duas latas a fim de garantir maior aproveitamento temos:\n- 18L: {contador18}\n- 3.6L: {contador3_6}\nNesse caso o valor pago será: "
      f"R$ {(contador18*80)+(contador3_6*25)}")