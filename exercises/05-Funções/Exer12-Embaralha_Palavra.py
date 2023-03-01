"""
Embaralha palavra. Construa uma função que receba uma string como parâmetro e devolva outra string com os carateres 
embaralhados. Por exemplo: se função receber a palavra python, pode retornar npthyo, ophtyn ou qualquer outra 
combinação possível, de forma aleatória. Padronize em sua função que todos os caracteres serão devolvidos em caixa 
alta ou caixa baixa, independentemente de como foram digitados.
"""
def embaralha(string):
    from random import shuffle

    string_temp = list(str(string))
    shuffle(string_temp)
    pal_final = ''.join(string_temp)
    return pal_final


# Programa Principal
while True:
    string = str(input('Digite uma palavra para embaralhar: ')).upper()
    if string == '0':
        break
    print(embaralha(string))