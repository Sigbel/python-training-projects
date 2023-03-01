"""
Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. A classe deve possuir os seguintes atributos: 
número da conta, nome do correntista e saldo. Os métodos são os seguintes: alterarNome, depósito e saque; No construtor, 
saldo é opcional, com valor default zero e os demais atributos são obrigatórios.
"""
class ContaCorrente:
    def __init__(self, conta: int, correntista: str, saldo: float=0):
        self.conta = conta
        self.correntista = correntista
        self.saldo = saldo

    def alterarNome(self, novo_nome):
        print(f'#ALTERA NOME DO CORRENTISTA - ANTIGO: {self.correntista} / NOVO: {novo_nome}')
        self.correntista = novo_nome

    def deposito(self, valor):
        self.saldo = self.saldo + valor
        print(f'#DEPOSITO (R${valor:.2f}) - Saldo atual: R${self.saldo}')
    
    def saque(self, valor):
        if (self.saldo - valor) < 0:
            print(f'Saque inválido, somente é possível sacar mais R$ {self.saldo:.2f}')
        else:
            self.saldo = self.saldo - valor
        print(f'#SAQUE (R${valor:.2f}) - Saldo atual: R${self.saldo}')
        
a = ContaCorrente(36547, 'Luiza')
a.deposito(500)
a.saque(200)
a.saque(300)
a.alterarNome('Linda')