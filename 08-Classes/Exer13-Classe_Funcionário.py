"""
Classe Funcionário: Implemente a classe Funcionário. Um empregado tem um nome (um string) e um salário(um double). Escreva 
um construtor com dois parâmetros (nome e salário) e métodos para devolver nome e salário. Escreva um pequeno programa que 
teste sua classe.
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

empregado = str(input('Digite o nome do empregado: '))
salario = float(input('Digite o salário do empregado: '))

a = Funcionario(empregado, salario)
print(a.get_nome)
print(a.get_salario)
