"""
Exercício 2 - Classe: Quadrado

Classe Quadrado: Crie uma classe que modele um quadrado:

    a. Atributos: Tamanho do lado
    b. Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
"""
class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def muda_valor(self, novo_valor):
        print(f'Mudando valor para: {novo_valor}')
        self.lado = novo_valor

    def retorna_valor(self):
        print(f'Valor atual do lado: {self.lado}')

    def calc_area(self):
        print(f'Área: {self.lado * self.lado}')

a = Quadrado(10)
a.retorna_valor()
a.muda_valor(4)
a.retorna_valor()
a.calc_area()

b = Quadrado(20)
b.retorna_valor()
a.retorna_valor()