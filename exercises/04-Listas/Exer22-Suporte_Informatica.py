"""
Exercício 22 - Suporte Informática

Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com a intenção de fazer 
um levantamento nas sucatas encontradas nesta área. A primeira tarefa dele é testar todos os cerca de 200 mouses 
que se encontram lá, testando e anotando o estado de cada um deles, para verificar o que se pode aproveitar deles.
Foi requisitado que você desenvolva um programa para registrar este levantamento. O programa deverá receber um 
número indeterminado de entradas, cada uma contendo: um número de identificação do mouse o tipo de defeito:

1. necessita da esfera;
2. necessita de limpeza; 
3. necessita troca do cabo ou conector; 
4. quebrado ou inutilizado 

*Uma identificação igual a zero encerra o programa. 

Ao final o programa deverá emitir o seguinte relatório:

Quantidade de mouses: 100

Situação                        Quantidade              Percentual
1- necessita da esfera                  40                     40%
2- necessita de limpeza                 30                     30%
3- necessita troca do cabo ou conector  15                     15%
4- quebrado ou inutilizado              15                     15%
"""

mouses = []
defeitos = []

c = 0
while True:
    mouse = str(input('Identificação mouse (0 para sair): '))
    mouses.append(mouse)

    if mouse =='0':
        break

    defeito = int(input('Código do defeito (1 a 4): '))
    while defeito < 0 or defeito > 4:
        defeito = int(input('Digite um código válido: '))
    defeitos.append(defeito)
    
    c += 1

print()
print(f'Quantidade de mouses: {c}\n')
print('Situação'.ljust(40), 'Quantidade'.ljust(12),'Percentual'.ljust(12))
print('1- necessita de esfera'.ljust(40),f'{defeitos.count(1)}'.ljust(12),f'{(defeitos.count(1)*100)/c:.2f}'.ljust(12))
print('2- necessita de limpeza'.ljust(40), f'{defeitos.count(2)}'.ljust(12), f'{(defeitos.count(2)*100)/c:.2f}'.ljust(12))
print('3- necessita troca de cabo ou conector'.ljust(40), f'{defeitos.count(3)}'.ljust(12), f'{(defeitos.count(3)*100)/c:.2f}'.ljust(12))
print('4- quebrado ou inutilizado'.ljust(40), f'{defeitos.count(4)}'.ljust(12), f'{(defeitos.count(4)*100)/c:.2f}'.ljust(12))
