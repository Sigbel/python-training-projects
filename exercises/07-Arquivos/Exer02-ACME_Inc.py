"""
A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos. Para 
tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários, e identificar 
os usuários com maior espaço ocupado. Através de um programa, baixado da Internet, ele conseguiu gerar o seguinte 
arquivo, chamado "usuarios.txt":

alexandre       456123789
anderson        1245698456
antonio         123456456
carlos          91257581
cesar           987458
rosemary        789456125

Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo, você deve criar um programa que gere um 
relatório, chamado "relatório.txt", no seguinte formato:

ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso

1    alexandre       434,99 MB             16,85%
2    anderson       1187,99 MB             46,02%
3    antonio         117,73 MB              4,56%
4    carlos           87,03 MB              3,37%
5    cesar             0,94 MB              0,04%
6    rosemary        752,88 MB             29,16%

Espaço total ocupado: 2581,57 MB
Espaço médio ocupado: 430,26 MB

O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, caso sejam necessários, de forma a 
agilizar a execução do programa. A conversão da espaço ocupado em disco, de bytes para megabytes deverá ser feita através 
de uma função separada, que será chamada pelo programa principal. O cálculo do percentual de uso também deverá ser feito 
através de uma função, que será chamada pelo programa principal.
"""
usuarios = {}

with open('02_usuarios.txt', 'r') as file:
    for c1 in file:
        nome = c1[0:15].replace(' ', '')
        espaco = c1[15:].replace(' ', '')
        espaco = (int(espaco)/1048576)
        usuarios.update({nome: f'{espaco:.2f}'})

with open('02_Relatório_ACME.txt', 'w+') as file2:
    file2.write('ACME INC.'.ljust(24))
    file2.write('Uso do espaco em disco pelos usuarios\n')
    file2.write('-'*72)
    file2.write('\nNr.'.ljust(6))
    file2.write('Usuario'.ljust(15))
    file2.write('Espaco utilizado'.ljust(21))
    file2.write('% do uso'.ljust(8))
    file2.write('\n\n')

    soma = 0
    for valores in usuarios.items():
        soma += float(valores[1])

    c = 1
    for k, c3 in usuarios.items():
        file2.write(f'{c}'.ljust(5))
        file2.write(f'{k}'.ljust(12))
        file2.write(f'{c3}'.rjust(16))
        file2.write('MB'.rjust(3))
        file2.write(f'{(float(c3) * 100)/soma:.2f} %'.rjust(13))
        file2.write('\n')
        c += 1

    file2.write(f'\nEspaco total ocupado: {soma:.2f} MB\n')
    file2.write(f'Espaco medio ocupado: {soma/(c-1):.2f} MB')
