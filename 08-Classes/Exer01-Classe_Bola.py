"""
Classe Bola: Crie uma classe que modele uma bola:

    a. Atributos: Cor, circunferência, material
    b. Métodos: trocaCor e mostraCor
"""

class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self, cor):
        self.cor = cor
        
    def mostraCor(self):
        print(f'Cor atual: {self.cor}')

a = Bola('azul', 70, 'plástico')
a.trocaCor('verde')
a.mostraCor()
a.trocaCor('rosa')
a.mostraCor()
