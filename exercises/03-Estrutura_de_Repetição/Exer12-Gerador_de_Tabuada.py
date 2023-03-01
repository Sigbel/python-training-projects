"""
Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
Tabuada de 5:

5 X 1 = 5
5 X 2 = 10
...
5 X 10 = 50
"""

num = int(input("A tabuada de qual número deseja visualizar? (1 a 10): "))

while 1 > num or num > 10:
    num = int(input("Digite um número entre 1 e 10.\nTente novamente: "))
print(f"Tabuada de {num}:")
for n in range(11):
    print(f"{num} x {n} = {num * n}")
