"""
Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de 
trânsito. Foram obtidos os seguintes dados:

A. Código da cidade;
B. Número de veículos de passeio (em 1999);
C. Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
D. Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
E. Qual a média de veículos nas cinco cidades juntas;
F. Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.
"""

acidentes_maior = 0
acidentes_menor = 0
cod_acidentes_menor = 0
cod_acidentes_maior = 0
c = 0
soma_veiculos = 0
soma_acidentes = 0
c_acidentes = 0

for n in range(5):
    cod = int(input(f"Digite o código da {n+1}ª cidade: "))
    num_veiculos = float(input(f"Digite o número de véiculos de passeio na {n+1}ª cidade: "))
    num_acidentes = float(input(f"Digite o número de acidentes na {n+1}ª ciade: "))
    while c < 1:
        acidentes_menor = num_acidentes
        cod_acidentes_menor = cod
        c += 1
# Definição de num_acidentes maior
    if num_acidentes > acidentes_maior:
        acidentes_maior = num_acidentes
        cod_acidentes_maior = cod
# Definição de num_acidentes menor
    if num_acidentes < acidentes_menor:
        acidentes_menor = num_acidentes
        cod_acidentes_menor = cod
    soma_veiculos = soma_veiculos + num_veiculos
    if num_veiculos < 2000:
        soma_acidentes = soma_acidentes + num_acidentes
        c_acidentes += 1
    print()

print("De acordo com as estatísticas, em 1999 obteve-se os seguintes dados: ")

print (f"Cidade com mais acidentes: Código {cod_acidentes_maior} / Número: {acidentes_maior}")
print (f"Cidade com menos acidentes: Código {cod_acidentes_menor} / Número: {acidentes_menor}")
print()
print(f"A média de veículos das 5 cidades juntas é: {soma_veiculos/5}")
print()
print(f"A média de acidentes nas cidades com menos de 2000 veículos é {soma_acidentes/c_acidentes}")
