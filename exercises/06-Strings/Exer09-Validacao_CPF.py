"""
Verificação de CPF. Desenvolva um programa que solicite a digitação de um número de CPF no formato 
xxx.xxx.xxx-xx e indique se é um número válido ou inválido através da validação dos dígitos verificadores 
e dos caracteres de formatação.
"""
valores_teste_dig = []
cont1, cont2 = 10, 11

cpf = input('Digite o CPF (somente números): ')
""" # Verificação de CPF (não obrigatório)
while not cpf.isnumeric():                      
    cpf = input('O CPF não pode conter ponto ou hífen.\nTente novamente: ')
while len(cpf) != 11:
    cpf = input('O CPF deve conter 11 números.\nTente novamente: ')"""
cpf_digitos1 = cpf[:-2]

# Verifica digito 1
for c1 in cpf_digitos1:
    valores_teste_dig.append((int(c1)*cont1))
    cont1 -= 1

teste_digito1 = 11 - (sum(valores_teste_dig) % 11)

digito1 = 0 if teste_digito1 > 9 else teste_digito1

valores_teste_dig = []
cpf_digitos2 = cpf_digitos1 + str(digito1)

#Verifica digito 2
for c2 in cpf_digitos2:
    valores_teste_dig.append((int(c2)*cont2))
    cont2 -= 1

teste_digito2 = 11 - (sum(valores_teste_dig) % 11)

digito2 = 0 if teste_digito2 > 9 else teste_digito2

novo_cpf = cpf_digitos2 + str(digito2)
print('CPF válido.') if novo_cpf == cpf else print('CPF Inválido.')
