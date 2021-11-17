"""
Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 
127 -> 721
"""
def reverso(numero):
    str_temp = str(numero)
    lista_temp = []
    for c1 in str_temp:
        lista_temp.append(c1)
    lista_temp.reverse()
    num_reverso = int(''.join(lista_temp))
    return num_reverso

# Programa Principal
num = int(input('Digite um número inteiro: '))
print(reverso(num))