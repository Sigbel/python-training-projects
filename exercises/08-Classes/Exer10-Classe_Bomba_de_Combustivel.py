"""
Exercício 10 - Classe: Bomba de Combustível

Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:

    a. Possua uma classe chamada bombaCombustível, com no mínimo esses atributos: Ø
        i. tipoCombustivel.
       ii. valorLitro
      iii. quantidadeCombustivel

    b. Possua no mínimo esses métodos:
        i. abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi 
           colocada no veículo
       ii. abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago 
           pelo cliente.
      iii. alterarValor( ) – altera o valor do litro do combustível.
       iv. alterarCombustivel( ) – altera o tipo do combustível.
        v. alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.

OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba.
"""
class bombaCombustivel:
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.tipoComb = tipoCombustivel
        self.valorLitro = valorLitro
        self.qtdeComb = quantidadeCombustivel

    @property
    def get_qtdeComb(self):
        return self.qtdeComb
    
    @property
    def get_tipo(self):
        return self.tipoComb

    def abastecerPorValor(self, valor):
        print(f'Abastecimento por Valor\nValor informado: R$ {valor:.2f}\n'
        f'QTDE de Litros: {valor/self.valorLitro:.2f} L\n')
        if self.qtdeComb - (valor/self.valorLitro) <= 0:
            print(f'Combustível insuficiente, favor reabastecer a Bomba.')
            return
        self.qtdeComb = self.qtdeComb - (valor/self.valorLitro)

    def abastecerPorLitro(self, qtdeLitros):
        print(f'Abastecimento por Litro\nQTDE informada: {qtdeLitros} L\n'
        f'Valor a ser pago: R${self.valorLitro*qtdeLitros:.2f}\n')
        if (self.qtdeComb - qtdeLitros) <= 0:
            print(f'Combustível insuficiente, favor reabastecer a Bomba.')
            return
        self.qtdeComb = self.qtdeComb - qtdeLitros
        

    def alterarValor(self, n_valor):
        print(f'Combustível Atual: {self.tipoComb}\nValor alterado:\n\t De:{self.valorLitro} | Para: {n_valor}')
        self.valorLitro = n_valor

    def alterarCombustivel(self, n_t_combustivel):
        print(f'Tipo de combustível alterado:\n\tDe: {self.tipoComb} | Para: {n_t_combustivel}')
        self.tipoComb = n_t_combustivel

    def alterarQuantidadeCombustivel(self, n_qtdeComb):
        print(f'Quantidade Atual de Combustível: {self.qtdeComb}')
        print(f'Quantidade alterada para: {n_qtdeComb}')
        self.qtdeComb = n_qtdeComb

a = bombaCombustivel('Gasolina', 5.60, 100)
while True:
    print('MENU'.center(50, '-'))
    print(f'Combustível na Bomba: {a.get_tipo} | QTDE: {a.get_qtdeComb} L')
    print('-'*50)
    opcao_1 = int(input('O que deseja fazer?\n\t1 - Abastecer (p/R$)\n\t2 - Abastecer (p/L)\n\t3 - Menu da Bomba'
    '\n\t4 - Sair\nComando: '))
    while opcao_1 != 1 and opcao_1 != 2 and opcao_1 != 3 and opcao_1 != 4:
        opcao_1 = int(input('Digite uma opção válida: '))
    if opcao_1 == 1:
        valor = float(input('Digite o valor em R$ a ser abastecido: '))
        print()
        a.abastecerPorValor(valor)
    elif opcao_1 == 2:
        litros = float(input('Digite a qtde em Litros a ser abastecido: '))
        print()
        a.abastecerPorLitro(litros)
    elif opcao_1 == 3:
        while True:
            opcao_2 = int(input('Menu da Bomba:\n\t1 - Alterar Valor\n\t2 - Alterar tipo de Combustível\n\t'
            '3 - Alterar Quantidade de Combustível\n\t4 - Voltar\nComando: '))
            while opcao_2 != 1 and opcao_2 != 2 and opcao_2 != 3 and opcao_2 != 4:
                opcao_2 = int(input('Digite uma opção válida: '))
            if opcao_2 == 1:
                valor = float(input('Digite o novo valor para o combustível em R$: '))
                a.alterarValor(valor)
            elif opcao_2 == 2:
                lista_comb = ['Gasolina', 'Gasolina Aditivada', 'Etanol', 'Diesel', 'GNV']
                combustivel = int(input('Selecione um combustível da lista:'
                '\n\t1 - Gasolina\n\t2 - Gasolina Aditivada\n\t3 - Etanol\n\t4 - Diesel\n\t5 - GNV\nComando: '))
                a.alterarCombustivel(lista_comb[combustivel-1])
            elif opcao_2 == 3:
                valor = float(input('Digite a nova qtde de combustível na bomba: '))
                a.alterarQuantidadeCombustivel(valor)
            else:
                break
    else:
        break        

