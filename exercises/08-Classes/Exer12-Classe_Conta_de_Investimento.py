"""
Classe Conta de Investimento: Faça uma classe contaInvestimento que seja semelhante a classe contaBancaria, com a diferença 
de que se adicione um atributo taxaJuros. Forneça um construtor que configure tanto o saldo inicial como a taxa de juros. 
Forneça um método adicioneJuros (sem parâmetro explícito) que adicione juros à conta. Escreva um programa que construa uma 
poupança com um saldo inicial de R$1000,00 e uma taxa de juros de 10%. Depois aplique o método adicioneJuros() cinco vezes 
e imprime o saldo resultante.
"""
class Conta_de_Investimento:
    def __init__(self, conta: int, correntista: str, saldo: float = 1000, juros = 10):
        self.conta = conta
        self.correntista = correntista
        self.saldo = saldo
        print(f'Saldo inicial configurado para R${saldo:.2f}')
        self.juros = juros
        print(f'Juros inicial configurado para {juros}%')

    def adicioneJuros(self):
        self.saldo = self.saldo + (self.saldo * self.juros/100)
        print(f'Novo valor: R${self.saldo}')

usuario = str(input('Digite o nome do responsável: '))
conta = int(input('Digite a conta: '))

a = Conta_de_Investimento(conta, usuario)
a.adicioneJuros()
a.adicioneJuros()
a.adicioneJuros()
a.adicioneJuros()
a.adicioneJuros()
