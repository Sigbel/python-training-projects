"""
Exercício 14 - Aprimoramento de Classe (Funcionário)

Aprimore a classe do exercício anterior para adicionar o método aumentarSalario (porcentualDeAumento) que aumente o salário 
do funcionário em uma certa porcentagem.

Exemplo de uso:
  harry=funcionário("Harry",25000)
  harry.aumentarSalario(10)
"""

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    @property
    def get_nome(self):
        return f'Nome do Funcionário: {self.nome}'

    @property
    def get_salario(self):
        return f'Salário de {self.nome}: R${self.salario}'

    def aumentarSalario(self, porcentual):
        print(f'Aumento de {porcentual}%: ')
        print(f'\tSalario Antigo: R${self.salario}')
        self.salario = self.salario + (self.salario * porcentual/100)
        print(f'\tSalário com Reajuste: R${self.salario}')

empregado = str(input('Digite o nome do empregado: '))
salario = float(input('Digite o salário do empregado: '))

a = Funcionario(empregado, salario)
print(a.get_nome)
print(a.get_salario)
a.aumentarSalario(10)
print(a.get_salario)