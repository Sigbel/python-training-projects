"""
Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da
operação deve ser acompanhado de uma frase que diga se o número é:

    A. par ou ímpar;
    B. positivo ou negativo;
    C. inteiro ou decimal.
"""

num_01 = input("Digite o primeiro número: ")
num_02 = input("Digite o segundo número: ")

resultado = 0
try:
    num_01 = int(num_01)
    num_02 = int(num_02)
except:
    try:
        num_01 = float(num_01)
        num_02 = float(num_02)
    except:
        print("Erro")

operacao = str(input("Digite a operação que deseja realizar ((+) Soma/(-) Subtração/(/) Divisão/(*) Multiplicação: "))
if operacao == "+":
    resultado = num_01+num_02
elif operacao == "-":
    resultado = num_01-num_02
elif operacao == "/":
    resultado = num_01/num_02
elif operacao == "*":
    resultado = num_01*num_02
else:
    print("Digite uma operação válida")

if resultado % 2 == 0:
    print("A. O resultado da operação é um número é par")
else:
    print("A. O resultado da operação é um número é ímpar")

if resultado >= 0:
    print("B. O resultado da operação é um número positivo.")
else:
    print("B. O resultado da operação é um número negativo.")

if type(resultado) == int:
    print("C. O resultado da operação é um número inteiro.")
elif type(resultado) == float:
    print("C. O resultado da operação é um número decimal.")