"""
Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o valor de H com N termos.
"""

n_termos = int(input("Digite o número de termos: "))
soma = 0

for n in range(n_termos):
    print(f"{1}/{n+1}", end="")
    soma = (1/(n+1)) + soma
    if n == n_termos-1:
        break
    print(" + ", end="")

print()
print(f"A soma da série é: {soma:.2f}")
