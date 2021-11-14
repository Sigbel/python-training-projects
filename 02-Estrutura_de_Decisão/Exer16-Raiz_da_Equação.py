"""
Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os
valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:

    a. Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
    b. Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
    c. Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
    d. Se o delta for positivo, a equação possui duas raizes reais; informe-as ao usuário;
"""
a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))

#ax² - bx - c
if a < 0:
    print("A  equação não é do segundo grau!")
else:
    calculo_delta = ((-b) ** 2) - (4 * a * c)
    raiz_1 = 0
    raiz_2 = 0
    if calculo_delta < 0:
        print(f"Raiz de {calculo_delta} não é um número real.")
    elif calculo_delta == 0:
        raiz_1 = (-(-b) + 0)/(2*a)
        print(f"A equação possui apenas uma raiz real, sendo igual a: {raiz_1:.2f}.")
    else:
        raiz_1 = ((-(-b) + (calculo_delta**(1/2)))/(2*a))
        raiz_2 = ((-(-b) - (calculo_delta**(1/2)))/(2*a))
        print(f"A equação possui duas raízes reais, sendo iguais a: {raiz_1:.2f} e {raiz_2:.2f} respectivamente.")