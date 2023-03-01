"""
Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de 
organizações:

"Qual o melhor Sistema Operacional para uso em servidores?"

As possíveis respostas são:

1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro

Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da 
mesma. O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. Não deverão 
ser aceitos valores além dos válidos para o programa (0 a 6). Os valores referentes a cada uma das opções devem ser 
armazenados num vetor. Após os dados terem sido completamente informados, o programa deverá calcular a percentual de 
cada um dos concorrentes e informar o vencedor da enquete. O formato da saída foi dado pela empresa, e é o seguinte:

Sistema Operacional     Votos   %
-------------------     -----   ---
Windows Server           1500   17%
Unix                     3500   40%
Linux                    3000   34%
Netware                   500    5%
Mac OS                    150    2%
Outro                     150    2%
-------------------     -----
Total                    8800

O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.
"""

sistema = ['Windows Server', 'Unix', 'Linux', 'Netware', 'Mac OS', 'Outro']
votos = [0,0,0,0,0,0]
c = 0

print('Qual o melhor Sistema Operacional para uso em servidores?\n\nAs possíveis respostas são:\n')
print('1 - Windows Server\n2 - Unix\n3 - Linux\n4 - Netware\n5 - Mac OS\n6 - Outro\n')

while True:
    voto = int(input("Digite seu voto (1 a 6) ou (0 para sair): "))
    while voto < 0 or voto > 6:
        voto = int(input('Informe um valor entre 1 e 6 ou 0 para sair: '))
    if voto == 0:
        break

    votos[voto-1] += 1
    c += 1

print()
print('Sistema Operacional'.ljust(25), 'Votos'.ljust(10), '%'.ljust(10))
print(''.ljust(20,'-'),' '*4, ''.ljust(7,'-'),' '*2, ''.ljust(7,'-'),' '*2)

for c1 in range(len(votos)):
    print(f'{sistema[c1]}'.ljust(25), f'{votos[c1]}'.ljust(10), f'{(votos[c1]*100)/c:.2f}'.ljust(10))

print(''.ljust(20,'-'),' '*4, ''.ljust(7,'-'),' '*2, ''.ljust(7,'-'),' '*2)
print('Total'.ljust(25), f'{c}\n')
print(f'O Sistema Operacional mais votado foi o "{sistema[votos.index(max(votos))]}", com {max(votos)} votos,'
      f' correspondendo a {(max(votos)*100)/c:.2f} % do total de votos.')
