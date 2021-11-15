"""
Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. 
Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.
"""

num_eleitores = int(input("Digite o númeor de eleitores: "))

c_flavio = 0
c_mauro = 0
c_algusto = 0

for n in range(num_eleitores):
    voto = int(input("Digite:\n1 - Flavio\n2 - Mauro\n3 - Algusto\n\nSeu voto: "))
    if voto == 1:
        c_flavio += 1
    if voto == 2:
        c_mauro += 1
    if voto == 3:
        c_algusto += 1

print(f"Flávio obteve {c_flavio} votos")
print(f"Mauro obteve {c_mauro} votos")
print(f"Algusto obteve {c_algusto} votos")
