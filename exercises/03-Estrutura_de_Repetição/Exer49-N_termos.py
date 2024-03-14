"""
Exercício 49 - N Termos

Faça um programa que mostre os n termos da Série a seguir:
  S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. 

Imprima no final a soma da série.
"""

n_termos = int(input("Digite o número de termos: "))
m = 1
soma = 0

for n in range(n_termos):
    print(f"{n+1}/{m}", end="")
    soma = ((n+1)/m) + soma
    if n == n_termos-1:
        break
    print(" + ", end="")
    m += 2

print()
print(f"A soma da série é: {soma:.2f}")
