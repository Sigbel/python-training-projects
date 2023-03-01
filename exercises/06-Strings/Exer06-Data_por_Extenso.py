"""
Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o 
nome do mês por extenso.

Data de Nascimento: 29/10/1973
Você nasceu em  29 de Outubro de 1973.
"""

def testa_data(data):
    meses = {31: {'Janeiro': 1, 'Março': 3, 'Maio': 5, 'Julho': 7, 'Agosto': 8, 'Novembro': 10, 'Dezembro': 12, },
             30: {'Abril': 4, 'Junho': 6, 'Setembro': 9, 'Novembro': 11},
             28: {'Fevereiro': 2}}
    data_modificada = data.replace('/', '')
    
    if len(data_modificada) > 8:
        return 'Erro: Data Inválida (Formato inválido)'
    if int(data_modificada[2:4]) > 13 or int(data_modificada[2:4]) < 1:
        return 'Erro: Data Inválida (Mes)'
    for c1 in meses:
        for k, elementos in meses[c1].items():
            if int(data_modificada[0:2]) > c1:
                return 'Erro: Data Inválida (Dia)'
    return str(data_modificada)


meses_selec = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto',
               'Setembro', 'Outubro', 'Novembro', 'Dezembro']

data = str(input('Data de Nascimento: '))

data_final = testa_data(data)
if data_final[0:4] != 'Erro':
    print(f'Você nasceu em {data_final[0:2]} de {meses_selec[int(data_final[2:4])-1]} de {data_final[4:8]}')
else:
    print(data_final)


