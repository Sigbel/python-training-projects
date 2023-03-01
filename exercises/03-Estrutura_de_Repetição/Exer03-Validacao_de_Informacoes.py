"""
Faça um programa que leia e valide as seguintes informações:

Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
"""

nome = input("Digite seu nome: ")
while len(nome) < 3:
    nome = input("O nome tem que conter mais que 3 caracteres.\nTente novamente: ")

idade = input("Digite um número entre 0 e 150: ")

while type(idade) != float:
    idade = input("Digite um valor númerico ou estar entre 0 e 150!\nTente novamente: ")
    if idade.isnumeric():
        idade = float(idade)
        while idade < 0 or idade > 150:
            idade = input("A idade deve estar entre 0 e 150.\nTente novamente: ")
            if idade.isnumeric():
                idade = float(idade)
            else:
                while type(idade) != float:
                    idade = input("Digite uma valor numérico!\nTente novamente: ")
                    if idade.isnumeric():
                        idade = float(idade)
                        continue
    continue
salario = input("Digite um sálario: ")

while type(salario) != float:
    salario = input("Digite um valor númerico!\nTente novamente: ")
    if salario.isnumeric():
        salario = float(salario)
        while salario < 0:
            salario = input("O salário deve ser maior que zero.\nTente novamente: ")
            if salario.isnumeric():
                salario = float(salario)
            else:
                while type(salario) != float:
                    salario = input("Digite uma valor numérico!\nTente novamente: ")
                    if salario.isnumeric():
                        salario = float(salario)
                        continue
    continue

sexo = input("Digite o Sexo - [M]asculino/[F]eminino: ").upper()
while True:
    sexo = input("Digite um valor válido.\nTente novamente: ").upper()
    if sexo == "F" or sexo == "M":
        break

estado_civil = input("Digite o estado civil - [s]olteiro, [c]asado, [v]iuvo, [d]ivorciado: ")

while True:
    estado_civil = input("Digite um valor válido.\nTente novamente: ").upper()
    if estado_civil == "S" or estado_civil == "C" or estado_civil == "V" or estado_civil == "D":
        break
