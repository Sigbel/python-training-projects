"""
Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.
Exemplo:
  12376489
  => 98467321
"""

num = int(input("Digite um número inteiro positivo: "))
c_num = num
c_com = 1

while c_com <= num:
    print(f"{c_com}" ,end=" ")
    c_com += 1
print()
print("=> ",end="")
while c_num > 0:
    print(f"{c_num}" ,end=" ")
    c_num -= 1
