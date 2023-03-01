"""
Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um 
dicionário com as seguintes informações:

- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)

Adicione também as docstrings da função
"""

def notas(*args, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    return: dicionário com várias informações sobre a situação da turma.
    """
    
    lista_notas = list(args)
    dic_notas = {}

    # Quantidade de notas
    dic_notas.update({'Total': len(lista_notas)})

    # Maior Nota
    dic_notas.update({'Maior': max(lista_notas)})

    # Menor Nota
    dic_notas.update({'Menor': min(lista_notas)})

    # Média da turma
    media = sum(lista_notas)/len(lista_notas)
    dic_notas.update({'Média': f'{media:.2f}'})
    
    if sit:
        if media == 10:
            dic_notas.update({'Situação': 'Excelente'})
        elif 7 <= media < 9:
            dic_notas.update({'Situação': 'Boa'})
        elif 6 <= media < 7:
            dic_notas.update({'Situação': 'Razoável'})
        elif media < 6:
            dic_notas.update({'Situação': 'Ruim'})
    
    return dic_notas

# Main Program
resp = notas(3.5, 2, 6.5, 2, 7, 4, sit=True)
print(resp)
