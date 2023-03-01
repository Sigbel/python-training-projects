"""
Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no 
formato D de mesPorExtenso de AAAA. Opcionalmente, valide a data e retorne NULL caso a data seja inválida.
"""


def mes(data):
    meses = {31: {'janeiro': 1,'março': 3,'maio': 5,'julho': 7,'agosto': 8,'novembro': 10,'dezembro': 12,},
    30:{'abril': 4, 'junho': 6, 'setembro': 9, 'novembro': 11},
    28:{'fevereiro': 2}}

    data_temp = list(str(data))
    while "/" in data_temp:
        data_temp.remove('/')
    dia_temp = ''.join(data_temp[0:2])
    mes_temp = ''.join(data_temp[2:4])
    ano_temp = ''.join(data_temp[4:8])

    if not len(data_temp) == 8: 
        return 'NULL'
    if int(mes_temp) > 12 or int(mes_temp) < 1:
        return 'NULL'

    for c1 in meses:
        for k, elementos in meses[c1].items():
            if int(dia_temp) > c1:
                return 'NULL'
            if int(mes_temp) == elementos:
                return f'{k} de {int(ano_temp)}'


# Programa Principal
while True:
    data_usuario = str(input('Digite uma data no formato "DD/MM/AAAA": '))
    if data_usuario == '0':
        break
    print(mes(data_usuario))
