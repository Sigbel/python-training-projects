"""
Exercício 8 - Classe: Macaco

Classe Macaco: Desenvolva uma classe Macaco,que possua os atributos nome e bucho (estomago) e pelo menos os métodos 
comer(), verBucho() e digerir(). Faça um programa ou teste interativamente, criando pelo menos dois macacos, alimentando-os 
com pelo menos 3 alimentos diferentes e verificando o conteúdo do estomago a cada refeição. Experimente fazer com que um 
macaco coma o outro. É possível criar um macaco canibal?
"""
class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []
        self.digestao = []

    def comer(self, comida):
        if self.digestao != []:
            print(f'O macaco {self.nome} preisa DIGERIR a comida anterior primeiro.')
            return
        print(f'O macaco {self.nome} COMEU um(a) {comida}')
        self.digestao.append(comida)

    def digerir(self):
        self.bucho.append(self.digestao[0])
        print(f'O macaco {self.nome} DIGERIU o(a) {self.digestao[0]}')
        self.digestao.pop()

    def verBucho(self):
        print(f'Comidas dentro do bucho de {self.nome}:')
        for c1 in self.bucho:
            print(f'\t{c1}')

a = Macaco('Wesley')
a.comer('maça')
a.comer('laranja')
a.digerir()
a.verBucho()
a.comer('laranja')
a.digerir()
a.verBucho()
a.comer('banana')
a.digerir()
a.verBucho()
print('-------------------')

b = Macaco('Kaio')
b.comer('abacate')
b.digerir()
b.verBucho()
b.comer('limão')
b.digerir()
b.verBucho()
b.comer('tomate')
b.digerir()
b.verBucho()
print('-------------------')

a.comer(b)
a.digerir()
a.verBucho()